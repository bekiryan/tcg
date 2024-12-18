import os

from openai import OpenAI

from tcg.code_generation import generate_code, validate_generated_code
from tcg.utils import get_all_files, extract_code, load_code_from_files


class TestCaseGenerator:
    def __init__(self, api_key: str, code_language: str = "Python", model: str = "gpt-4o", validate: bool = False):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.validate = validate
        self.language = code_language

    def generate(self, function_description: str, code_paths: list[str], output_file_path: str) -> None:
        # Get all files from directories or file paths
        code_files = load_code_from_files(get_all_files(code_paths), code_paths)

        response = generate_code(self.client, code_files,self.language, function_description, self.model)
        test_code = extract_code(response)
        print("Generated test code:", test_code)

        if self.validate:
            validate = validate_generated_code(self.client, test_code,self.language, self.model)
            print("Validation:", validate)
            if "Validation Summary: Failed" in validate:
                print("Validation failed. Regenerating code.")
                response = generate_code(self.client, test_code + validate, function_description, self.model)
                test_code = extract_code(response)


        # Ensure the directory exists
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # Write the generated code to a file
        with open(output_file_path, "w") as file:
            file.write(test_code)

        print(f"Generated test code saved to {output_file_path}")

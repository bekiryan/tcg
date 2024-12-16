import os
import argparse
from tcg.code_generation import generate_code, validate_generated_code
from tcg.utils import get_all_files, load_code_from_files, extract_code


def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Generate test code based on given parameters.")
    parser.add_argument("--function_description", type=str, required=True, help="Description of the function to test.")
    parser.add_argument("--code_paths", type=str, nargs="+", required=True,
                        help="Paths to one or more code files or directories.")
    parser.add_argument("--output_file_path", type=str, required=True, help="Output path for the generated test file.")

    args = parser.parse_args()

    # Get all files from directories or file paths
    code_files = get_all_files(args.code_paths)

    response = generate_code(load_code_from_files(code_files), args.function_description)
    test_code = extract_code(response)
    print(test_code)
    validate = validate_generated_code(test_code)
    print(validate)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(args.output_file_path), exist_ok=True)

    # Write the generated code to a file
    with open(args.output_file_path, "w") as file:
        file.write(test_code)

    print(f"Generated test code saved to {args.output_file_path}")


if __name__ == "__main__":
    main()

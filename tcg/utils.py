import os
import re
import glob


def get_all_files(file_or_dir_paths):
    """Collects all files from given paths, whether they are files, directories, or patterns."""
    all_files = []
    for path in file_or_dir_paths:
        if '*' in path or '?' in path:
            all_files.extend(glob.glob(path, recursive=True))
        elif os.path.isfile(path):
            all_files.append(path)
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                all_files.extend(os.path.join(root, file) for file in files)
    return all_files


def load_code_from_files(file_paths, code_paths):
    """Loads and concatenates code content from specified code files, handling encoding errors."""
    code_content = ""
    for file_path, code_path in zip(file_paths, code_paths):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                code_content += f"# {code_path}\n"
                code_content += file.read() + "\n\n"  # Separate files with newlines
        except UnicodeDecodeError:
            print(f"Skipping non-UTF-8 file: {file_path}")
    return code_content


def extract_code(response):
    # Regex to capture content between ```python and ```
    match = re.search(r"```(?:python)?\s*(.*?)```", response, re.DOTALL)
    if match:
        return match.group(1).strip()  # Extract and strip any surrounding whitespace
    return response.strip()  # Return original if no code block is found

from .llm import chat_completion


def generate_code(client, code, language="Python", description="", model="gpt-4o"):
    prompt = f"""
    You are a unit test generator specializing in creating high-quality unit tests for {language} programming language.
    Your task is to generate all possible unit tests functions or methods for a given code snippet.

    #### **Expected Output:**
    - A unit test file containing tests functions or methods for the provided code snippet.
    - The output will adhere to the conventions and libraries of the specified programming language.
      For example:
        - Python: Use `unittest` or `pytest`.
        - Java: Use `JUnit`.
        - JavaScript/TypeScript: Use `Jest` or `Mocha`.
        - C#: Use `xUnit` or `NUnit`.

    #### **Test Code Structure Requirements:**
    1. **Test Function or Method Names**:
        - Follow the naming conventions of the specified language (e.g., `test_` prefix for Python, camelCase for Java).
        - Include descriptive names that reflect the purpose of the test.
        - Combine all test functions or methods into a single class or module.

    2. **Test Cases**:
        - Cover typical inputs, edge cases, and invalid inputs.
        - Use assertions to verify expected behavior.

    3. **Descriptions**:
        - Add comments or docstrings explaining the purpose of each test case.

    #### Example Input Code:
    **Your Function:**
    ```{language}
    {code}
    ```

    **Test Case Descriptions:**
    {description}

    #### **Expected Test Code Output:**
    - Generate unit tests using the conventions of the `{language}` language.
    """
    print(f"Generating test code for: {description}")
    return chat_completion(client, prompt, model)


def validate_generated_code(client, generated_code, language="Python", model="gpt-4o"):
    prompt = f"""
    You are a code validator specializing in checking the correctness of unit tests for {language} programming language.
    Your task is to validate the provided unit test code against the following requirements:

    #### **Validation Requirements:**

    1. **Test Function or Method Names**:
        - Verify that test names follow the naming conventions of the `{language}` language.

    2. **Test Case Coverage**:
        - Ensure the test cases cover:
          - Typical inputs.
          - Edge cases.
          - Invalid inputs (if applicable).

    3. **Test Code Structure**:
        - Verify that all required imports or setup are present.
        - Ensure that test cases use appropriate assertions to verify correctness.
        - Check for meaningful comments or docstrings explaining the purpose of each test case.

    4. **Use of Language-Specific Testing Libraries**:
        - Ensure the appropriate testing framework is used (e.g., `unittest` or `pytest` for Python, `JUnit` for Java, `Jest` for JavaScript).

    5. **Formatting**:
        - Code should be syntactically correct and free of errors.
        - Code should be well-organized and adhere to the conventions of the `{language}` language.

    #### **Validation Task:**

    1. Receive the unit test code in `{language}` to validate.
    2. Compare the code against the requirements listed above.
    3. Return a validation report that includes:
       - A summary of whether the code passed or failed validation.
       - Details on any specific issues found in the code (e.g., missing test cases, naming issues, incorrect use of testing libraries).
       - Suggestions for improving the code if any issues are detected.

    #### Example Validation Output:
    1. Validation Summary: Passed

    Details:
        - Test names follow `{language}` conventions.
        - Test cases cover typical inputs, edge cases, and invalid inputs.
        - Correct use of `{language}` testing libraries.
        - Code is well-structured and formatted.

    2. Validation Summary: Failed
    
    Details:
        - Missing test cases for edge cases.
        - Incorrect use of assertions in test functions.
        - Test names do not follow `{language}` conventions.
        
    Suggestions:
        - Add test cases for edge cases to improve coverage.
        - Use appropriate assertions to verify expected behavior.
        - Update test function names to adhere to `{language}` conventions.
    #### Input Code for Validation:
    ```{language}
    {generated_code}
    ```

    Return a validation report following the structure of the example output above.
    """
    return chat_completion(client, prompt, model)

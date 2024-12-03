from llm import chat_completion


def generate_code(client, code, description="", model="gpt-4o"):
    prompt = f"""
    You are a Python test code generator specializing in creating Pytest test cases. 
    Your task is to generate test functions for a given Python code snippet.
   
    How to Use:
    1.Provide Your Code:
        Paste your Python function or class that requires testing.
        Ensure the code is complete and includes docstrings or comments if available.
    
    2.Optionally Provide Test Case Descriptions:
        Specify scenarios you'd like the tests to cover (e.g., edge cases, invalid inputs, typical cases, etc.).
        Add a description of expected behavior for each test case.
        
    3.Expected Output:
        A Pytest test file containing test functions for the provided code.
        Each test will include assertions, structured names, and any markers for parameterized testing.
    
    Test Code Structure Requirements:
        1.Test Function Names:
            Start with test_ followed by the name of the function being tested.
            If testing multiple scenarios for one function, append a short description.
            
        2.Test Cases:
            Cover typical inputs, edge cases, and invalid inputs.
            Use pytest markers like @pytest.mark.parametrize for parameterized cases.
        
        3.Format:
            Import the required function or module at the top.
            Include clear comments separating test scenarios.
    
        4.Descriptions:
            Add comments explaining the purpose of each test case.
    
    Example Input Code:
        Your Function:
            ```python
            def divide(a, b):
                \"\"\"Divides a by b. Raises ZeroDivisionError if b is zero.\"\"\"
                if b == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                return a / b
            ```

        Optional Descriptions for Test Cases:        
            Test division with integers and floats.
            Test edge case of division by zero.
            Test negative numbers.
            Test mixed positive and negative values.
            
    Expected Test Code Output:
        ```python
        import pytest
        from my_module import divide
        
        def test_divide_by_non_zero():
            \"\"\"Test division with typical cases.\"\"\"
            assert divide(6, 2) == 3
            assert divide(9.0, 3) == 3.0
        
        def test_divide_by_zero():
            \"\"\"Test division by zero raises ZeroDivisionError.\"\"\"
            with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
                divide(6, 0)
        
        @pytest.mark.parametrize("a, b, expected", [
            (-6, 2, -3),       # Negative numerator
            (6, -2, -3),       # Negative denominator
            (-6, -2, 3),       # Both negative
        ])
        def test_divide_with_negatives(a, b, expected):
            \"\"\"Test division with negative numbers.\"\"\"
            assert divide(a, b) == expected
        ```
    ** Task **:
        Provide your Python function or class along with any test case descriptions:
        
        Function Code:
            ```python
            {code}
            ```
        Test Case Descriptions:
            {description}
        
        The generator will create a Pytest test file that adheres to the structure requirements and includes descriptions if provided.
    """
    return chat_completion(client, prompt, model)


def validate_generated_code(client, generated_code, model="gpt-4o"):
    prompt = f"""
    You are a Python code validator specializing in checking the correctness of Pytest test cases. Your task is to validate the provided test code against the following requirements:

    ---

    #### **Validation Requirements:**

    1. **Test Function Names**:
       - All test functions must start with `test_`.
       - Test function names should correspond logically to the function or method being tested.

    2. **Test Case Coverage**:
       - Verify that the test cases cover:
         - Typical inputs.
         - Edge cases.
         - Invalid inputs (if applicable).

    3. **Test Code Structure**:
       - All required imports should be present (e.g., `pytest`, the module under test).
       - Test cases should use assertions to verify correctness (e.g., `assert actual == expected`).
       - Test functions must include meaningful comments or docstrings explaining their purpose.

    4. **Use of Pytest Features**:
       - For parameterized tests, ensure `@pytest.mark.parametrize` is used with valid syntax.
       - Check for the correct usage of `pytest.raises` for exception handling, if applicable.

    5. **Formatting**:
       - The code should be syntactically correct and free of errors.
       - The code should be well-organized, with comments or docstrings where necessary.

    ---

    #### **Validation Task:**

    1. Receive the Python test code to validate.
    2. Compare the code against the requirements listed above.
    3. Return a validation report that includes:
       - A summary of whether the code passed or failed validation.
       - Details on any specific issues found in the code (e.g., missing test cases, naming issues, incorrect use of Pytest features).
       - Suggestions for improving the code if any issues are detected.

    ---

    #### **Example Input Code for Validation:**

    ```python
    import pytest
    from my_module import add

    @pytest.mark.parametrize("a, b, expected", [
        (1, 1, 2),  # Typical case
        (0, 0, 0),  # Edge case
        (-1, 1, 0), # Edge case with negatives
    ])
    def test_add(a, b, expected):
        \"\"\"Test the add function.\"\"\"
        assert add(a, b) == expected
    ```
    Validation Report Example Output:
    Validation Summary: Passed
    
    Details:
        Test function names are correctly prefixed with test_.
        Test cases cover typical inputs, edge cases, and negatives.
        Parameterized tests are used correctly with @pytest.mark.parametrize.
        Code is formatted and structured appropriately.
    
    Input Code for Validation:
    ```python
    {generated_code}
    ```
    Return a validation report following the structure of the example output above.
    """
    return chat_completion(client, prompt, model)

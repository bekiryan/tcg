def chat_completion(client, message, model="gpt-4o"):
    """A helper function to interact with OpenAI's chat completion API.

    :param client: OpenAI: The OpenAI client to use for the completion.
    :param message: str: The message to send to the model.
    :param model: str: The model to use for the completion.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content.strip()


def local_chat_completion(message):
    #TODO: Implement local chat completion
    # llm = OllamaLLM(model="deepseek-coder-v2", base_url="http://localhost:11434", device_map="auto")
    # print(
    #     f"Generating test code for prompt: {prompt_template.invoke({'retrieved_tests': retrieved_tests, 'function_description': function_description, 'code': code_content})}")
    # sequence = prompt_template | llm
    # generated_code = sequence.invoke({
    #     "retrieved_tests": retrieved_tests,
    #     "function_description": function_description,
    #     "code": code_content
    # })
    # return generated_code
    ...

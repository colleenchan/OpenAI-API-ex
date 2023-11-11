import openai
import os

def get_gpt4_response(prompt, api_key):
    try:
        openai.api_key = api_key
        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

def main():
    # Retrieve API keys from environment variables
    api_key1 = os.getenv('OPENAI_API_KEY1')

    # Check if the API keys are set
    if not api_key1 or not api_key2:
        print("Error: API keys are not set in the environment variables.")
        return

    # Choose which API key to use
    api_key_choice = input("Choose API key (1 or 2): ")
    api_key = api_key1 if api_key_choice == '1' else api_key2

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = get_gpt4_response(user_input, api_key)
        print("GPT-4:", response)

if __name__ == "__main__":
    main()

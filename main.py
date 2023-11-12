import openai
import os

def get_gpt4_chat_response(prompt, api_key):
    try:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return str(e)

def main():
    # Retrieve API key from environment variable
    api_key = os.getenv('SDS617_API_KEY')

    # Check if the API key is set
    if not api_key:
        print("Error: The API key is not set in the environment variables.")
        return

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = get_gpt4_chat_response(user_input, api_key)
        print("GPT-4:", response)

if __name__ == "__main__":
    main()
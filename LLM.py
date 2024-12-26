import openai
from apiKey import call_api

def main():
    # Define the question you want to ask the model
    prompt = "What is the capital of India?"
    print(prompt)
    response = call_api(prompt)
    print(response)

if __name__ == "__main__":
    main()

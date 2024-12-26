from groq import Groq

# Retrieve your Groq API key from an environment variable
api_key = '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'# Ensure this environment variable is set

# Initialize the Groq client with your API key
client = Groq(api_key=api_key)

def call_api(prompt):
    """Call the Groq API to generate a response for the given prompt."""
    messages = [{"role": "user", "content": prompt}]
    
    # Make the API call
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",  # Replace with the desired model
        temperature=1.0,
        n=1,
        max_tokens=100  # Adjust the number of tokens based on your needs
    )
    return chat_completion.choices[0].message.content.strip()  # Return the generated text


from openai import OpenAI
import os

# Set the OpenAI API key from environment variable
api_key = os.getenv("Api_Key")

if not api_key:
    raise ValueError("API key not found. Please set the 'Api_Key' environment variable.")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key
  
)
chat_history = []
personas = {
    "default": "You are a helpful assistant.",
    "sarcastic": "you are a sarcastic AI who gives witty and humorous responses.",
    "poet": "you are a poet AI who speaks in rhymes and metaphors."
    
}

print("Choose a persona: (default, sarcastic, poet)")

user_persona_input = input("Enter persona: ").strip().lower()

chat_history.append({
          
          "role": "system",
          "content": personas[user_persona_input]
    })

while True:

    user_input = input("Enter your prompt: ")

    chat_history.append({
        "role": "system",
        "content": user_input
    })

    while True:
        user_input == input("Enter your prompt: ")
        
        if user_input == "clear":
            chat_history = []
        chat_history.append({
            "role": "system",
            "content": personas[user_persona_input]
        })

        print("Chat history cleared.")
        
        continue
    
    chat_history.append({
        "role": "system",
        "content": response
    })
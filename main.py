from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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", ##api key
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

    if user_input == "exit":
        break
    
    completion = client.chat.completions.create(
    
    model="deepseek/deepseek-r1-zero:free",
    messages=chat_history
    )

    response = completion.choices[0].message.content
    print(response)    
    
    chat_history.append({
        "role": "system",
        "content": response
    })

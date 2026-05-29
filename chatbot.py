from groq import Groq

client = Groq(api_key="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")

print("Chatbot ready! 'quit' likho band karne ke liye")

while True:
    user_input = input("Tum: ")
    
    if user_input.lower() == "quit":
        break
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    
    print("Bot:", response.choices[0].message.content)
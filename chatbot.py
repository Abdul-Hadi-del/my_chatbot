from groq import Groq

client = Groq(api_key="YOUR_API_KEY_HERE")

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
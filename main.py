# main.py
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

print("🤖 Gemini Chat Assistant (powered by uv!)")
print("Type 'quit', 'exit', or 'bye' to stop\n")

# Get API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: Set GEMINI_API_KEY environment variable!")
    print("Example: $env:GEMINI_API_KEY =", api_key)
    exit(1)

client = genai.Client(api_key=api_key)

# Fast & current model in 2026
MODEL = "gemini-2.5-flash"   # or "gemini-2.5-flash-lite" for even faster/cheaper

chat = client.chats.create(model=MODEL)

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Goodbye! 👋")
        break
    
    if not user_input:
        continue
    
    try:
        response = chat.send_message(user_input)
        print(f"Gemini: {response.text}\n")
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Check key, quota, or model name.")
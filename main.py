import os
import google.generativeai as genAi
from dotenv import load_dotenv

# Load .env
load_dotenv()

#configure gemini
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error : GEMINI_API_KEY not found in .env file")

genAi.configure(api_key=api_key)

model = genAi.GenerativeModel('gemini-1.5-flash')

print("🤖 Gemini Chat Assistant")
print("Type 'exit' or 'quit' to stop\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Goodbye! 👋")
        break
    
    if not user_input:
        continue
    
    try:
        response = model.generate_content(user_input)
        print("\nGemini:", response.text.strip())
        print("-" * 60)
    except Exception as e:
        print("Error:", str(e))

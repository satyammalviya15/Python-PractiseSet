import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Configure your valid API key
genai.configure(api_key=api_key)

# Use a supported model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# Prompt
prompt = "What is 2 + 2?"
try:
    response = model.generate_content(prompt)
    print("Gemini says:", response.text)
except Exception as e:
    print("Error:", e)

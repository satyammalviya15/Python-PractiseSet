import pyautogui
import pyperclip
import time
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Configure your valid API key
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")


# Optional: A short delay to allow the user to prepare
time.sleep(3)

# Step 1: Click on the icon
pyautogui.click(x=960, y=1043)
time.sleep(2)  # Wait for the app to open

# Step 2: Drag to select text
pyautogui.moveTo(686, 237)
pyautogui.mouseDown()
pyautogui.moveTo(707, 950, duration=0.5)
pyautogui.mouseUp()

# Step 3: Press Ctrl+C to copy
pyautogui.hotkey('ctrl', 'c')

# Step 4: Get clipboard content
copied_text = pyperclip.paste()

prompt = copied_text + "responce like you are satyam"
try:
    response = model.generate_content(prompt)
    print("Gemini says:", response.text)
except Exception as e:
    print("Error:", e)

pyperclip.copy(response.text)

pyautogui.click(802,973)

pyautogui.hotkey('ctrl','v')

pyautogui.press('enter')

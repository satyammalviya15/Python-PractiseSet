import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import pyjokes
import pyautogui
import os
import subprocess
os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")
import vlc
import yt_dlp
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# 🔑 Set API key
genai.configure(api_key=api_key)  # Replace with your Gemini API key

def gemini_chat(prompt_text):
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
        response = model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Initialize Text to Speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def greet():
    now = datetime.datetime.now()
    hour = now.hour
    date = now.strftime("%A, %d %B %Y")
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak(f"Today is {date}. The time is {now.strftime('%I:%M %p')}")
    speak("I am Jarvis. How may I assist you?")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening You")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
        except sr.WaitTimeoutError:
            speak("No voice detected. Please try again.")
            return ""
    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-IN')  # English India
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please say it again.")
    except sr.RequestError:
        speak("Unable to connect to the internet. Please check your connection.")
    return ""

def run_jarvis():
    greet()
    while True:
        command = listen()
        if not command:
            continue

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}.")

        elif 'date' in command:
            date = datetime.datetime.now().strftime("%A, %d %B %Y")
            speak(f"Today's date is {date}.")

        elif 'wikipedia' in command:
            speak("Searching Wikipedia...")
            topic = command.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(topic, sentences=2, auto_suggest=False)
                speak(result)
            except wikipedia.exceptions.DisambiguationError:
                speak("Please be more specific, multiple results found.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any results.")

        elif 'play' in command:
            song = command.replace("play","").strip()
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)

        elif 'aaj tak' in command:
            url = "https://www.youtube.com/watch?v=Nq2wYlWFucg"  # Aaj Tak
            streamlink_path = r"C:\Users\satya\AppData\Roaming\Python\Python312\Scripts\streamlink.exe"
            subprocess.call([streamlink_path, url, 'worst'])
  
            # url = "https://www.youtube.com/watch?v=Nq2wYlWFucg"  # Aaj Tak standard link
            # ydl_opts = {'format': 'bestaudio/best','quiet': True,
            #             'extract_flat': False,'noplaylist': True}
            # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            #     info = ydl.extract_info(url, download=False)
            #     audio_url = info['url']
            #     title = info.get('title', 'Unknown')
            #     print("Now playing:", title)
            #     player = vlc.MediaPlayer(audio_url)
            #     player.play()

        elif 'search' in command:
            query = command.replace("search", "").strip()
            speak(f"Searching {query} on Google.")
            pywhatkit.search(query)

        elif 'open youtube' in command:
            speak("Opening YouTube.")
            pywhatkit.search("YouTube")

        elif 'close' in command or 'minimize' in command :
            pyautogui.hotkey('winleft','m')

        elif 'tell me a joke' in command or 'joke' in command:
            joke = pyjokes.get_joke(language='en', category='all')
            speak("Here it is: " + joke)

        elif 'screenshot' in command:
            image = pyautogui.screenshot()
            image.save("screenshot.png")
            speak("Screenshot taken and saved.")

        elif 'note this' in command or 'take a note' in command:
            speak("What should I note down?")
            note = listen()
            if note:
                with open("jarvis_notes.txt", "a", encoding="utf-8") as f:
                    f.write(f"{datetime.datetime.now()}: {note}\n")
                speak("Note saved.")

        elif 'stop' in command or 'bye' in command or 'exit' in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("I am ask to Gemini?")
            speak("Thinking...")
            answer = gemini_chat(command)
            speak("Here is the response:")
            speak(answer)


# Run Jarvis
if __name__ == "__main__":
    run_jarvis()

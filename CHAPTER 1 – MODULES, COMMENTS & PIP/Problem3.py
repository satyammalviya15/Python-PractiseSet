# 3. Install an external module and use it to perform an operation of your interest. 

# run on terminal pip install pyjokes

import pyjokes
print(pyjokes.get_joke())

import pyttsx3
engine = pyttsx3.init()
engine.say("It's Er Satyam Malviya is speaking")
engine.runAndWait()
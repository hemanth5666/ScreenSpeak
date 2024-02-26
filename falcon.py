"pywin32,pypi,pypiwin32,win32,pypive,pyttsx3==2.7"
import pyttsx3

def talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

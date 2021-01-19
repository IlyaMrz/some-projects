import sys
import pyttsx3
text = sys.argv[1]
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id) # Joey IVONA 2 en
engine.setProperty('rate', 245)
engine.say(text)
engine.runAndWait()
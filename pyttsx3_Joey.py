import sys
import pyttsx3
text = sys.argv[1]
try: speed = int(sys.argv[2])
except: speed = 245
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id) # Joey IVONA 2 en
engine.setProperty('rate', speed)
engine.say(text)
engine.runAndWait()
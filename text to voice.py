import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[1].id) :for girl voice 
engine.setProperty('rate', 130)
engine.say("Hello World")
engine.runAndWait()

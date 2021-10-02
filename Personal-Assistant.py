import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():# This will wish me just after starting according to time period of day
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! your name")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! your name")   

    else:
        speak("Good Evening! your name")  

    speak("I am Edith . Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):# for connecting with email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'Password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:# searching anything in wikipedia
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
# these function will run according to way you want to query
        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif  'open google' in query:
            webbrowser.open("google.com") 

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'what is time going on' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:# path of application should be given 
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to s' in query:# forsending emails
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "**************@gmail.com"    # email adress
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")  
        
        elif 'email to dad' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "*********@gmail.com"    # email adress
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")  
        # You can add various queries according to your need

        elif 'what is your name' in query:
            speak("My name is Edith")   


        elif 'your favourite food' in query:
            speak("chicken tandoor and biryani")   


        elif 'who are you' in query:
            speak("sasmit's personal assistant")
        
        elif 'how can you help me' in query:
            speak("I can sed email! , I can open google , youtube , stackoverflow , and search wikipedia for you")
            
        
        else:
            quit

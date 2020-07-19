import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>0 and hour <=12:
        speak("Good morning!")
    elif hour> 12 and hour<=18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("Sir, I am Jarvis. Please tell me how can I help you")

def takeCommand():
    '''
    it takes microphone input from users and returns output
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        text = r.recognize_google(audio)

    except Exception as e:
        # print(e)

        print("say that again please")
        return "None"
    return text


def sendEmail():
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.startls()
    server.login('youremail@gmail.com','your-password')
    server.senmail('youremail@gmail.com',to, content)
    server.close()




if __name__=="__main__":
    wishMe()
    while True:
        #     logic for executing tasks based on query
        text = takeCommand().lower()
        if 'wikipedia' in text:
            speak("Searching Wikipedia..")
            text = text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=2)
            speak("According to wikipedia.")
            print(results)
            speak(results)

        elif 'open youtube' in text:
            webbrowser.open("youtube.com")

        elif 'open google' in text:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in text:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in text:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            for i in songs:
               value = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[value]))

        elif 'the time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code' in text:
            codePath = "C:\\Users\\Vedant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in text:
            try:
                speak("What should I say?")
                content= takeCommand()
                to = "Vedantyouremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email at the moment")

        elif 'quit' in text:
            sys.exit(speak("Thank you sir, I shall take my leave now"))



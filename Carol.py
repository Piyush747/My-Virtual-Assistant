import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import winsound
import time

engine = pyttsx3.init('sapi5')  #enable voice function
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):  #take audio input from user 
    engine.say(audio)
    engine.runAndWait()

def wishme():  #checks the time and wishes 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning [your name]")
    elif hour>=12 and hour<18:
        speak("Good Afternoon [your name]")
    else:
        speak("Good Evening [your name]")
    speak("I Am Carol, your virtual assistant. Please tell me how can i help you")
def takeCommand(): 
    #it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print("You Said...",query)
    except Exception as e:
        #print(e)
        print("Say that again please")
        return "None"
    return query
def sendEmail(to,content):  #it logs in to your gmail account and sends mail as per your request
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','yourpassword')
    server.sendmail('youremail.gmail.com',to,content)
    server.close()
def alarm(set_alarm_timer): #sets alarm as per your request
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M")
        date = current_time.strftime(r"%d/%m/%Y")
        if now == set_alarm_timer:
            speak("Wake up sir")
            music_dir = 'C:\\alarmtones' #path to your music folder
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
            break

if __name__=='__main__':
    wishme()  #calling the wish me function
    while True:
        query = takeCommand().lower()  #takes audio input and stores it in form of lower case string
        #logic for executing task based on query
        if 'wikipedia' in query:  #searches on wiki and speaks out first 2 sentences on your requested topic
            speak("Searching Wikipedia\n")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wiki...")
            print(results)
            speak(results)
        elif "open youtube" in query:  #opens youtube on your default browser
            webbrowser.open("youtube.com")
        elif "open google" in query:  #opens google on your default browser
            webbrowser.open("google.com")
        elif "open gmail" in query:  #opens gmail on your default browser
            webbrowser.open("gmail.com")

        elif "play music" in query:  #plays music for you
            music_dir = 'C:\\music' #path to your music folder
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randrange(0,119)]))  #randomly plays a song for you

        elif "the date" in query:  #tells you the date today
            now = datetime.datetime.now()
            date = now.strftime(r"%m/%d/%Y")
            speak(f"today is {date}")
        elif "day" in query:  #tells you the day today
            now = datetime.datetime.now()
            day = now.strftime("%A")
            speak(f"Today is {day}")
        elif "time now" in query:  #tells you the time now
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif "open code" in query:  #opens vs code for you
            code_path = "C:\\Users\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif "who are you" in query:  #tells about herself
            speak("I am carol, your virtual assistant")
        elif "you can rest now" in query:  #to close the program
            speak("Okay [your name]. bye")
            break
        elif "set an alarm" in query:  #to set an alarm on your desired time (still under progress)
            speak("at what time")
            alarmTime = (takeCommand())
            if len((alarmTime))==4:
                minutes = (alarmTime[-2:])
                hours = (alarmTime[:-2])
                alarm_time = f"{hours}:{minutes}"
                speak("your alarm will ring at {} hours and {} minutes ".format(hours,minutes))
                alarm(alarm_time)
                
        elif "mail to me" in query: #to send email to yourself
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "youremail@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry i am not able to send the mail. Please try again")





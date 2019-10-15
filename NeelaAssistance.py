import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import re
from random import randint

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser = webbrowser.get('chrome')


def store(query):
    with open("interaction.txt", "a+") as f:
        f.write(query + "\n")
        f.close()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am 'NEELA', Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("speak that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mohicomputer8@gmail.com', 'rbu@2017')
    server.sendmail('maddywiz1998@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query

        # code to open browser  and stuff
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube in your browser")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open stack over flow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'search' in query:
            speak("searching your query")
            webbrowser.open(query)

        # code to open videos and music
        elif 'video' in query:
            video_dir = 'D:\song videos'
            videos = os.listdir(video_dir)
            if 'any' in query:
                speak("playing a video of my choice sir")
                os.startfile(os.path.join(video_dir, videos[randint(0, len(videos))]))
            else:
                ls = query.split()
                str, c = "", 0
                for x in ls:
                    if re.match("play", x) or re.match("video", x) or re.match("song", x):
                        pass
                    else:
                        str = str + " " + x

                str = str.strip()
                print(str)
                for x in range(len(videos)):
                    if re.match(str, videos[x].lower()):
                        speak("playing your videos sir")
                        c = 1
                        os.startfile(os.path.join(video_dir, videos[x]))
                        break
                if (c == 0):
                    speak("sir, your video is not present on the system. should i open web")
                    query2 = takeCommand().lower()
                    if 'yes' in query2 or 'search' in query2:
                        webbrowser.open("https://google.com/search?q=%s" % query)
        elif 'music' in query or 'song' in query:
            music_dir = 'D:\Musics'
            songs = os.listdir(music_dir)
            if 'any' in query:
                speak("playing a song of my choice sir")
                os.startfile(os.path.join(music_dir, songs[randint(0, len(songs))]))
            else:
                ls = query.split()
                str, c = "", 0
                for x in ls:
                    if re.match("play", x) or re.match("song", x):
                        pass
                    else:
                        str = str + " " + x

                str = str.strip()
                print(str)
                for x in range(len(songs)):
                    if re.match(str, songs[x].lower()):
                        speak("playing your song sir")
                        c = 1
                        os.startfile(os.path.join(music_dir, songs[x]))
                        break
                if (c == 0):
                    speak("sir, your song is not present on the system. should i open web")
                    query2 = takeCommand().lower()
                    if 'yes' in query2 or 'search' in query2:
                        webbrowser.open("https://google.com/search?q=%s" % query)

        # code to date time management
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%d:%B:%Y")
            speak(f"Sir, the date is {strDate}")
        elif 'day' in query:
            strDay = datetime.datetime.now().strftime("%A")
            speak(f"Sir, today is {strDay}")

        # code to open applications
        elif 'open paint' in query:
            speak("opening paint")
            codePath = "C:\Windows\System32\mspaint.exe"
            os.startfile(codePath)
        elif 'open android studio' in query:
            speak("opening android studioes")
            codePath = "C:\Program Files\Android\Android Studio\\bin\studio64.exe"
            os.startfile(codePath)
        elif 'open code' in query:
            speak("opening code")
            codePath = "D:\Computer Softwares\\vscode\code.exe"
            os.startfile(codePath)
        elif 'open excel' in query:
            speak("opening MS Excel")
            codePath = "C:\Program Files\Microsoft Office\\root\Office16\EXCEL.EXE"
            os.startfile(codePath)

        elif 'open word' in query:
            speak("opening Word")
            codePath = "C:\Program Files\Microsoft Office\\root\Office16\WINWORD.EXE"
            os.startfile(codePath)

        elif 'open power point' in query:
            speak("opening Power Point")
            codePath = "C:\Program Files\Microsoft Office\\root\Office16\POWERPNT.EXE"
            os.startfile(codePath)

        elif 'open google chrome' in query:
            speak("opening Chrome")
            codePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)

        elif 'open team viewer' in query:
            speak("opening TeamViewer")
            codePath = "C:\Program Files (x86)\TeamViewer\TeamViewer.exe"
            os.startfile(codePath)

        elif 'open my computer' in query:
            speak("opening my Computer")
            #codePath ="C:\Users\DELL\Desktop\ThisPC"
            os.startfile(codePath)


        # interaction with pc
        elif 'shut down' in query:
            speak("shutting down your system,Sir!")
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            speak("restarting your system, sir!")
            os.system("shutdown /r /t 1")
            break

        # neela interaction code
        elif 'who are you' in query or 'define yourself' in query:
            speak('''i m Neela your personal assistance. Im here to make your life easier.
            You can command me perform various tasks such as calculating sums or opening applications, playing songs and 
            videos and searching web and many more things.''')
        elif 'who made you' in query or 'created you' in query:
            speak("I have been created by Mohit Sharma.")
        elif 'hello' in query or 'hi' in query or 'hey' in query:
            speak("Hellow Sir, What can i do for you!")
            store(query)
            # speak("hello  bahi    kese  ho   tum.")
        elif 'how are you' in query:
            speak("I am fine, what about you sir.")
            store(query)
        elif 'you are cool' in query:
            speak("i always knew it.")
            store(query)
        elif 'i am fine' in query or 'i am also fine' in query:
            speak("that's great. How was your day then")
            store(query)
        elif 'fuck you' in query :
            speak("fuck you too ")

        # code to send email
        elif 'email to ' in query:
            try:
                speak("What should I speak?")
                content = takeCommand()
                to = "maddywiz1998@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend maddy bhai. I am not able to send this email")

        # code to exit neela
        elif 'stop' in query or 'quit' in query or 'close' in query:
            speak("oh! okay. Goodbye SIR! ")
            break;
        else:
            print(query)
            speak("I didn't understand that. But if you want i can search that on google")
            query2 = takeCommand().lower()
            if 'yes' in query2 or 'search' in query2:
                webbrowser.open("https://google.com/search?q=%s" % query)

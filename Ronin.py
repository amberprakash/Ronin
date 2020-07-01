import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    if hour>=12 and hour<18 :
        speak("Good Afternoon!")
    elif hour>18 and hour<24 :
        speak("good evening!")

    speak("I am ronin sir. Please tell me how may i help you")
    speak("")
    
     

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=500
        r.dynamic_energy_threshold=500
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en=in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"

    return query            

wishMe()
print("1. You can search any query by saying {sachin tendulkar wikipedia } and it will give you information about your query\n 2.You can open youtube by saying {Open youtube}\n 3.You can open google by saying {open google} and it will open google for you \n4.It can also tell you time by saying {the time}" )
while True:
    query=takeCommand().lower()
    if 'wikipedia' in query:
        speak('searching wikipedia')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    #elif 'search google':
      #  speak("what! would you like to search")
       # print("for searching speak - search whatever")
       # ket=takeCommand().lower()
       # speak("searching")
       # ket=ket.replace("search","")
       # webbrowser.open(f"youtube.com/results?search_query={ket}")


    elif 'open google' in query:
        webbrowser.open("google.com")  

    elif 'play music' in query:
        music_dir = 'D:\\MUSIC'
        songs = os.listdir(music_dir)
        n=len(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f" Sir, The time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Microsoft VS Code.exe"
        os.startfile(codePath)

    elif 'thank you' in query:
        break
      




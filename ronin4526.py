import pyttsx3
import speech_recognition as sr
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        r.dynamic_energy_threshold=600
        r.energy_threshold=450
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        print(e)
        speak("utter clearly")
        print("utter clearly")
        return "None"

    return query            


speak("I am Ronin983922 and I am here to assist you ")  
speak(" I am straight forward and don't make me angry")

speak("tell me your name")
name=takeCommand().lower()
if 'amber' in name:
    speak("You are my master ")
    speak("Sorry master for above interogation but i will keep your data safe and protected")
    speak("Do you want me to play music for you")
    ans=takeCommand().lower()
    if 'yes' in ans:
        music_dir = 'D:\\MUSIC'
        songs = os.listdir(music_dir)
        n=len(songs)
        a=int(n)
        actual = random.randint(songs[0],songs[a-1])
        os.startfile(os.path.join(music_dir,actual))

    else:
        speak("Sorry")
            

else:
    speak("you are not my master ")
    speak(f"{name}, whats your purpose to come here")
    query=takeCommand().lower()
    if 'music' in query:
        music_dir = 'D:\\MUSIC'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[0]))    


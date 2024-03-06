import pyttsx3
import speech_recognition as sr
import random
import pyjokes
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',  200) 


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')  # Corrected language code
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    return query



def sad():
    speak("what happened sir")
    emotion = takecommand()
    if "lost my job" in emotion:
        speak("Don’t worry, you are very talented, you can find new job easily")
    elif "death" in emotion:
        speak("I am sorry to hear that. Death is a natural part of life, you should take rest")
    else:
        speak("Don’t worry, I’m here with you. you want to listen a joke")
        play_joke =takecommand()
        if  "yes" in play_joke:
            jokes = pyjokes.get_jokes()
            joke = random.choice(jokes)
            speak(joke)
                    
        else :
            speak("Don’t worry,  you want to listen a song")
            play_music =takecommand()
            if "yes" in play_music: 
                music_dir="C:\\Users\\Gaurakh\\Desktop\\audio"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir,rd))
            else:
                speak("what do you want sir")
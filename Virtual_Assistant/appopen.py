import pyautogui
import pyttsx3
import os
import cv2
import random
import webbrowser
import pywhatkit
import pyttsx3
import speech_recognition as sr

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



def notepad():
    npath = "C:\\Windows\\System32\\notepad.exe"
    os.startfile(npath)  

def opencamera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        if img is not None and img.shape[0] > 0 and img.shape[1] > 0:
            cv2.imshow("mycam", img )
            k = cv2.waitKey(50)
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()  

def music():
    music_dir="C:\\Users\\Gaurakh\\Desktop\\audio"
    songs = os.listdir(music_dir)
    rd = random.choice(songs)
    os.startfile(os.path.join(music_dir,rd))
def opengoogle():
    speak("sir, what should i search on google")
    cm=takecommand().lower()
    if  cm == "" or "nothing" in cm:
        webbrowser.open("http://www.google.com")
    else:
        webbrowser.open(f"{cm}") 

def youtube(query):
    speak("This is what I found for your search!") 
    youtube_word =["youtube search","youtube","jarvis", "friday"]
    for keyword in youtube_word:
        query = query.replace(keyword, "")
    web  = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done, Sir") 

def open_youtube():
    speak("Sir, what should I search on YouTube?")
    search_query = takecommand().lower()
    if search_query:
        youtube_url = f"https://www.youtube.com/results?search_query={search_query}"
        webbrowser.open(youtube_url) 
    elif "nothing" or "" in  search_query:
         webbrowser.open("https://www.youtube.com/")     
         

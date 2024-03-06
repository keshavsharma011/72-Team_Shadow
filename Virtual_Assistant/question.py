import pyttsx3
import speech_recognition as sr
import datetime


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
def sleep():
    hour  = int(datetime.datetime.now().hour)
    if hour >= 2 and hour <= 14:
        speak("okk sir, have a good day")
    elif hour >= 14 and hour <= 20:
        speak("okk sir, good evening")
    else:
        speak("okk sir, it's very late. Have a good night.")
        
def greetMe():
    hour  = int(datetime.datetime.now().hour)
    time = datetime.datetime.now()
    formatted_time = time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
        speak(f"Good Morning sir, its {formatted_time}")
    elif hour >12 and hour<=18:
        speak(f"Good Afternoon sir, its {formatted_time}")
    else:
        speak(f"Good Evening sir, its {formatted_time}")
    speak("I am friday, please tell me How can I help you ?")        
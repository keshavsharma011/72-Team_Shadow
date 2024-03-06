import pyttsx3
import speech_recognition as sr
import wikipedia

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
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    return query









def search_wikipedia(query):
    speak("Searching from Wikipedia....")
    WIKIPEDIA_KEYWORDS = ["wikipedia", "search wikipedia", "friday", "according to", "find out about",  "learn more about",]
    for keyword in WIKIPEDIA_KEYWORDS:
        query = query.replace(keyword, "")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia..")
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results. Please be more specific.")
    except wikipedia.exceptions.PageError as e:
        speak("Sorry, I could not find information on that topic.") 
        
        
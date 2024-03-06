import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
from requests import get


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





def temprature():
    speak("sir please tell me loaction")
    loca=takecommand()
    search =f"temperature in {loca}"
    url =f"https://www.google.com/search?q={search}"
    r =requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div",class_="BNeawe").text
    speak(f"current {search} is {temp}")





def ipaddress():
    ip = get('https://api.ipify.org').text
    speak(f"your ip address is{ip}")


def news():
    speak("how  much news do you want?, like top 5")
    x = int(input("news"))
    main_url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0bcb90f1c58c4b6ab3b4238c1b5702a1"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eightn","ninth","tenth"]
    for ar in articles:
        head.append(ar['title'])
    for  i in range(x):
       
        speak(f"today's {day[i]} news is: {head[i]}")    
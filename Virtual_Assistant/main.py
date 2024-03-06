import pyttsx3
import speech_recognition as sr
import datetime
import schedule
import time
import os
import cv2
import random
import requests
from requests import get
import webbrowser
import pywhatkit
import smtplib
import pyjokes
import json
from urllib.request import urlopen
import pyautogui
from bs4 import BeautifulSoup
import psutil
from pywikihow import search_wikihow
import speedtest
from appopen import *
from feeling import *
from osfile import *
from scrap import *
from question import *
from search import *
from callmsg import *
from personal import *
from reminder import *
from openapp import *
from googlescrap import *
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

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

function_active = False

if __name__ == "__main__":
    while True:
        query = takecommand().lower()

        if "activate" in query or "friday" in query or "wake up" in query:
            greetMe()
            while True:
                schedule.run_pending()
                time.sleep(1)
                query = takecommand().lower()

                if "open notepad" in query or "open text editor" in query:
                    notepad()
                elif "command prompt" in query or 'terminal' in query:
                    os.system("start cmd")
                elif "open camera" in query or "selfie" in query or "photo" in query:
                    opencamera()
                elif "play music" in query or "listen song" in query:
                    music()
                elif "ip address" in query or "internet address" in query:
                    ipaddress()
                elif "wikipedia" in query:
                    search_wikipedia(query)
                elif "open google" in query:
                    opengoogle()
                elif "open youtube" in query:
                    open_youtube()
                elif "youtube" in query:
                    youtube(query)
                elif "send message" in query:
                    whatmsg()
                    pyautogui.press('enter')
                elif "send mail" in query:
                    mail()
                elif "joke" in query:
                    jokes = pyjokes.get_joke()
                    speak(jokes)
                elif  "news"  in query:
                    news()    
                    
                elif "switch window" in query or "switch current window" in query:
                    switch_window()
                elif "switch tab" in query or "switch current tab" in query:
                    switch_tab()
                elif "shut down my computer" in query:
                    shutdown()
                    sleep()
                    speak("I am also going to sleep mode sir")
                    break
                elif 'restart my computer' in query:
                    restart()
                
                elif "temperature" in query:
                    temprature()
                elif "sleep" in query or "bye" in query:
                    sleep()
                    break
                elif "battery" in query:
                    batterypercentage()
                elif "internet speed" in query:
                    internetspeed()
                elif "feeling sad" in query:
                    sad()
                elif "close" in query:
                    close_app()
                elif 30 == battery_percentage and battery_status == False:
                    speak("Battery Critically Low, Please Charge Immediately")
                elif 15 == battery_percentage and battery_status == False:
                    speak("Battery is very Low, Please Charge Immediately")
                elif 10 == battery_percentage and battery_status == False:
                    speak("You don't have sufficient power, please plug-in your charger")
                elif "personal details" in query or "about member" in query or "project member" in query:
                    process_person(persons)
                elif "open" or "open chrome" in query  : 
                    open_applications_from_paragraph(query)  
                    
                        
                
                elif "shutdown" in query:
                    exit()
                        
                elif query != "":
                    speak(online_scraper(query))
                    
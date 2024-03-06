import pyttsx3
import speech_recognition as sr
import os
import psutil
import pyautogui
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

def internetspeed():
    speak("Hello, let me check the internet speed.")
    try:
        os.system('cmd /k "speedtest')
    except Exception as e:
        speak("Sorry, I couldn't check the internet speed at the moment.")
        print(e)
battery_percentage = psutil.sensors_battery().percent
battery_status = psutil.sensors_battery().power_plugged        
def batterypercentage():

    speak(f"sir battery is {battery_percentage}% charged")
    if battery_status == False:
        if battery_percentage ==  100:
            speak("Your Battery is fully Charged")
        elif 90 <= battery_percentage < 100:
            speak("Your Battery is Almost Fully Charged")
        elif  50 <= battery_percentage <  90:
            speak("don't worry sir you have sufficient power")
        elif  30 <= battery_percentage <  50:
            speak("Battery Critically Low, Please Charge Immediately")
        elif    15 <= battery_percentage <    30 :
            speak("Battery is very Low, Please Charge Immediately")
        elif  10 <= battery_percentage <  15:
            speak("sir, your system will shutdown soon, please plug-in your charger ")
        else: 
            speak("you don't have sufficient power, please plug-in your charger")
    else:
        speak("Laptop is currently charging.")        
   
def restart():
    os.system('shutdown /r /t 10')
    speak("Your computer will restart within 10 seconds")
def shutdown():
    speak("Your computer will shutting down in 15 second")
    os.system("shutdown /s /t 15")   

def switch_window():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt') 
def switch_tab():
    pyautogui.keyDown('ctrl')
    pyautogui.press('tab')
    pyautogui.keyUp('ctrl')
# def close_tab():
#     speak("Okay, sir")
#     pyautogui.keyDown('ctrl')
#     pyautogui.press('w')
#     pyautogui.keyUp('ctrl')

# def new_tab():
#     speak("Okay, sir")
#     pyautogui.keyDown('ctrl')
#     pyautogui.press('t')
#     pyautogui.keyUp('ctrl')

    
def close_app():
    speak = input("which application you want to to close : ")
    process_name= takecommand()
    
    for proc in psutil.process_iter(['pid', 'name']):
        if process_name.lower() in proc.info['name'].lower():
            try:
                # Terminate the process
                os.kill(proc.info['pid'], 9)
                print(f"Closed {proc.info['name']} (PID: {proc.info['pid']})")
            except Exception as e:
                print(f"Error closing {proc.info['name']}: {e}")                
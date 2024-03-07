import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import smtplib
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



def whatmsg():
    speak("Please provide the recipient's phone number.")
    recipient_contact = input("Recipient's Phone Number: ").strip()
    if recipient_contact:
        speak("What message would you like to send?")
        message_content = takecommand().lower()
        if message_content:
            speak(f"Sending message to {recipient_contact} with content: {message_content}")
            pywhatkit.sendwhatmsg(recipient_contact, message_content,datetime.datetime.now().hour, datetime.datetime.now().minute + 2)  # Adjusted wait time
        else:
            speak("No message content provided. Please try again.")
    else:
        speak("No recipient contact provided. Please try again.")









def sendmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        
        server.login('gparjapati097@gmail.com', 'shadow#gmail')

        server.sendmail("gparjapati097@gmail.com", to, content)
        server.close()
    except Exception as e:
        print(e)
        speak("Error occurred while sending email. Please try again.")
def mail():
    try:
        speak("what should i send")
        content=takecommand().lower()
        to=input('To:').strip()
        sendmail(to,content)
        speak("Email sent successfully")
    except Exception as e:
        print(e)
        speak("Error occurred while sending email. Please try again.")

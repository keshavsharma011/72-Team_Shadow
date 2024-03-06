import json
import pyttsx3
import speech_recognition as sr

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

class Person:
    def __init__(self, name, surname, occupation, description=""):
        self.name = name
        self.surname = surname
        self.occupation = occupation
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "occupation": self.occupation,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        name = data.get("name", "")
        surname = data.get("surname", "")
        occupation = data.get("occupation", "")
        description = data.get("description", "")
        return cls(name, surname, occupation, description)

    def get_details(self):
        return f"Name: {self.name}, Surname: {self.surname}, Occupation: {self.occupation}, Description: {self.description}"

    @classmethod
    def fetch_person_details(cls, persons_list, person_name):
        for person in persons_list:
            if person.name.lower() == person_name.lower():
                return person.get_details()

def fetch_person_description(person_name, persons_list):
    for person in persons_list:
        if person.name.lower() == person_name.lower():
            return person.description
    return None

def save_persons_to_file(persons_list):
    with open("persons.json", "w") as file:
        json.dump([person.to_dict() for person in persons_list], file)

def process_person(persons_list):
    search_name = takecommand().lower()
    description = fetch_person_description(search_name, persons_list)

    if description:
        speak(f"The description is: {description}. Do you want to know more about this person?")
        
        response = takecommand().lower()
        
        if "yes" in response:
            details = Person.fetch_person_details(persons_list, search_name)
            if details:
                speak(details)
            else:
                speak("Details not found.")
        else:
            speak("Okay, no more details provided.")

    else:
        speak(f"Person '{search_name}' not found. Do you want to add a new person?")

        response = takecommand().lower()
        
        if "yes"  or "yas" in response:
            speak("please tell me surname:")
            surname = takecommand()
            speak("please tell me occupation")
            occupation = takecommand()
            speak("please tell me description")
            description = takecommand()

            new_person = Person(search_name, surname, occupation, description)
            persons_list.append(new_person)

            speak(f"New person '{search_name}' added.")
        else:
            speak("Okay, no new person added.")

    save_persons_to_file(persons_list)

try:
    with open("persons.json", "r", encoding="utf-8") as file:
        persons_data = json.load(file)
        persons = [Person.from_dict(person) for person in persons_data]
except FileNotFoundError:
    persons = []

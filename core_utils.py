import pyttsx3
import speech_recognition as sr

# Configuration settings
assistant_name = "Leo"
voice_rate = 190  # Adjust this to match the desired speed of the assistant's voice

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init("sapi5")  # Use the SAPI5 engine for Windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Choose a female voice; change index for male voice
engine.setProperty('rate', voice_rate)  # Set the rate of speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand.")
            return ""
        except sr.RequestError:
            speak("There was an error with the recognition service.")
            return ""


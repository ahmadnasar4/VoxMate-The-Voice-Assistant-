from core_utils import speak, listen, detect_hotword
from greet import greet_user
from conversation import conversation
from web_search import web_search, google_search, youtube_search
from time import strftime
from temperature import check_temperature
from app_management import open_app, close_app
from youtube_control import set_volume, forward, backward, play_pause
from memory import remember, recall
from game import play_game
from volume import decrease_volume, increase_volume
from internet_speed import check_internet_speed
from shutdown import shutdown_system
import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Set to female voice
engine.setProperty("rate", 190)  # Speed of speech

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print(f"Recognized: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand.")
            return ""
        except sr.RequestError:
            speak("There was an error with the recognition service.")
            return ""

def display_menu():
    """Display the command menu to the user."""
    menu_text = (
        " Here are some things you can ask me:\n"
        " Search Google, YouTube, or Wikipedia.\n"
        " Check the current time.\n"
        " Check the current temperature.\n"
        " Open or close applications like Notepad or Chrome.\n"
        " Control YouTube playback: play, pause, forward, or backward.\n"
        " Adjust the volume or set it to a specific level.\n"
        " Remember and recall information.\n"
        " Play a game of Rock-Paper-Scissors.\n"
        " Shut down the system.\n"
        " Exit the assistant."
    )
    print(menu_text)
    speak(menu_text)

if __name__ == "__main__":
    greet_user()
    conversation()
    display_menu()

    while True:
        query = listen().lower()

        # Check if the query is valid
        if query == "":
            continue  # Skip to the next iteration if the command was not recognized

        try:
            # Web search commands

            if "google" in query:
                q = query.replace("search google", "").strip()
                google_search(q)
            elif "youtube" in query:
                q = query.replace("search youtube", "").strip()
                youtube_search(q)
            elif "wikipedia" in query:
                q = query.replace("search", "").strip()
                web_search(q)

            # System time check
            elif "time" in query:
                current_time = strftime("%H:%M:%S")  # Get current time
                speak(f"The current time is {current_time}.")
                print(f"Current time: {current_time}")

            # Temperature check
            elif "temperature" in query:
                check_temperature()

            # App management (open/close)
            elif "open" in query:
                app_name = query.replace("open", "").strip()
                open_app(app_name)
            elif "close" in query:
                app_name = query.replace("close", "").strip()
                close_app(app_name)

            # YouTube control
            elif "play" in query or "pause" in query:
                play_pause()
            elif "forward" in query:
                forward()
            elif "backward" in query:
                backward()
            elif "set volume to" in query:
                try:
                    level = int(query.split("set volume to")[-1].strip().replace("%", ""))
                    set_volume(level)
                except ValueError:
                    speak("Please specify a valid volume level.")

            # Volume control
            elif "volume up" in query:
                increase_volume()
            elif "volume down" in query:
                decrease_volume()

            # Memory functions
            elif "remember that" in query:
                parts = query.split("remember that")[-1].strip().split("is")
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    speak(remember(key, value))
                else:
                    speak("Please provide a valid statement to remember.")

            elif "what do you remember about" in query:
                key = query.replace("what do you remember about", "").strip()
                speak(recall(key))

            #internet speed
            elif "internet speed" in query or "check speed" in query:
                check_internet_speed()

            # Game
            elif "play game" in query or "rock paper scissors" in query:
                play_game()

            # System shutdown
            elif "shutdown" in query or "shut down the system" in query:
                shutdown_system()

            # Exit the assistant
            elif "exit" in query:
                speak("Goodbye! Have a great day.")
                break

            # Catch unrecognized commands
            else:
                speak("I'm sorry, I didn't understand that command. Please try again.")

        except Exception as e:
            # Handle any unexpected errors
            print(f"Error: {e}")
            speak("An error occurred while processing your command.")

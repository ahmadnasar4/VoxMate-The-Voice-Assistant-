import tkinter as tk
import pyttsx3
import speech_recognition as sr
import threading
from time import strftime
from greet import greet_user
from conversation import conversation
from web_search import web_search, google_search, youtube_search
from temperature import check_temperature
from app_management import open_app, close_app
from youtube_control import set_volume, forward, backward, play_pause
from memory import remember, recall
from game import play_game
from volume import decrease_volume, increase_volume
from internet_speed import check_internet_speed
from shutdown import shutdown_system

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Set to female voice
engine.setProperty("rate", 190)  # Speed of speech

# GUI output label to be updated in the GUI
output_label = None

def speak(text):

    engine.say(text)
    engine.runAndWait()
    update_output(text)

def update_output(text):

    output_label.config(text=text)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        update_output("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            update_output(f"Recognized: {command}")
            return command
        except sr.UnknownValueError:
            update_output("Sorry, I did not understand.")
            return ""
        except sr.RequestError:
            update_output("There was an error with the recognition service.")
            return ""

def process_query(query):

    try:
        if "google" in query:
            q = query.replace("search google", "").strip()
            update_output(f"Searching Google for: {q}")
            google_search(q)

        elif "youtube" in query:
            q = query.replace("search youtube", "").strip()
            update_output(f"Searching YouTube for: {q}")
            youtube_search(q)

        elif "wikipedia" in query:
            q = query.replace("search", "").strip()
            update_output(f"Searching Wikipedia for: {q}")
            web_search(q)

        elif "time" in query:
            current_time = strftime("%H:%M:%S")
            response = f"The current time is {current_time}."
            update_output(response)
            speak(response)

        elif "temperature" in query:
            response = check_temperature()
            update_output(response)
            speak(response)

        elif "open" in query:
            app_name = query.replace("open", "").strip()
            update_output(f"Opening {app_name}.")
            speak(f"Opening {app_name}.")
            open_app(app_name)

        elif "close" in query:
            app_name = query.replace("close", "").strip()
            update_output(f"Closing {app_name}.")
            speak(f"Closing {app_name}.")
            close_app(app_name)

        elif "play" in query or "pause" in query:
            update_output("Playing/Pausing video.")
            speak("Playing/Pausing video.")
            play_pause()

        elif "forward" in query:
            update_output("Forwarding video.")
            speak("Forwarding video.")
            forward()

        elif "backward" in query:
            update_output("Rewinding video.")
            speak("Rewinding video.")
            backward()

        elif "set volume " in query:
            try:
                level = int(query.split("set volume to")[-1].strip().replace("%", ""))
                update_output(f"Setting volume to {level}%.")
                speak(f"Setting volume to {level}%.")
                set_volume(level)
            except ValueError:
                update_output("Please specify a valid volume level.")
                speak("Please specify a valid volume level.")

        elif "volume up" in query:
            update_output("Increasing volume.")
            speak("Increasing volume.")
            increase_volume()

        elif "volume down" in query:
            update_output("Decreasing volume.")
            speak("Decreasing volume.")
            decrease_volume()

        elif "remember that" in query:
            parts = query.split("remember that")[-1].strip().split("is")
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                update_output(f"Remembering {key} as {value}.")
                speak(f"Remembering {key} as {value}.")
                remember(key, value)
            else:
                response = "Please provide a valid statement to remember."
                update_output(response)
                speak(response)

        elif "what do you remember about" in query:
            key = query.replace("what do you remember about", "").strip()
            response = recall(key)
            update_output(response)
            speak(response)

        elif "internet speed" in query or "check speed" in query:
            response = check_internet_speed()
            update_output(response)
            speak(response)

        elif "play game" in query or "rock paper scissors" in query:
            response = play_game()
            update_output(response)
            speak(response)

        elif "shutdown" in query or "shut down the system" in query:
            update_output("Shutting down the system.")
            speak("Shutting down the system.")
            shutdown_system()

        elif "exit" in query:
            update_output("Goodbye! Have a great day.")
            speak("Goodbye! Have a great day.")
            root.quit()

        else:
            update_output("I'm sorry, I didn't understand that command. Please try again.")
            speak("I'm sorry, I didn't understand that command. Please try again.")

    except Exception as e:
        update_output("An error occurred while processing your command.")
        speak("An error occurred while processing your command.")
        print(f"Error: {e}")

def listen_for_commands():
    """Listen for commands continuously and process them."""
    def recognize():
        query = listen()
        if query:
            process_query(query)
        root.after(1000, listen_for_commands)  # Restart listening after a small delay

    recognition_thread = threading.Thread(target=recognize)
    recognition_thread.daemon = True
    recognition_thread.start()

def create_gui():
    """Create the GUI window."""
    global root, output_label
    root = tk.Tk()
    root.title("Voice Assistant")
    root.geometry("600x500")

    # Simplified and concise permanent menu text
    menu_text = (
        "Voice Assistant Commands:\n"
        "- Google, YouTube, or Wikipedia search\n"
        "- Get current time or temperature\n"
        "- Open/close applications (e.g., Notepad, CMD)\n"
        "- Control YouTube: play, pause, forward, backward\n"
        "- Adjust or set volume\n"
        "- Memory: remember and recall info\n"
        "- Play Rock-Paper-Scissors\n"
        "- Check internet speed\n"
        "- Shutdown system or exit"
    )

    # Display the concise menu
    menu_label = tk.Label(root, text=menu_text, wraplength=500, justify="left", font=("Arial", 10), fg="gray")
    menu_label.pack(pady=10)

    # Create the output label to show responses
    output_label = tk.Label(root, text="", wraplength=500, justify="left", font=("Arial", 12))
    output_label.pack(pady=20)

    # Start greeting, conversation, then display the menu
    update_output("Starting Greeting...")
    greet_user()
    conversation()

    # Start listening for commands
    listen_for_commands()

    root.mainloop()

if __name__ == "__main__":
    create_gui()

import os
from core_utils import speak
from core_utils import listen

def shutdown_system():
    speak("Are you sure you want to shut down the system? Please confirm.")
    confirmation = listen()
    if "yes" in confirmation or "confirm" in confirmation:
        speak("Shutting down the system. Goodbye!")
        os.system("shutdown /s /t 5")  # Shuts down after a 5-second delay
    else:
        speak("Shutdown canceled.")

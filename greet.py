from core_utils import speak

def greet_user():
    """Greet the user based on the time of day."""
    import time
    hour = int(time.strftime("%H"))
    if hour < 12:
        speak("Good morning!")
        print("Good morning!")

    elif 12 <= hour < 18:
        speak("Good afternoon!")
        print("Good afternoon!")

    else:
        speak("Good evening!")
        print("Good evening!")

    print("How can I assist you today?")
    speak("How can I assist you today?")

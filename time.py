import datetime
from core_utils import speak

def time():
    current_time = datetime.strftime("%H:%M")
    speak(f"The time is {current_time}")

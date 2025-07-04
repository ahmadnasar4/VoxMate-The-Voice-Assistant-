import pyautogui
from core_utils import speak
import time

def play_pause():

    pyautogui.press("k")
    speak("Playback toggled.")

def forward():

    pyautogui.press("l")
    speak("Skipped forward.")

def backward():

    pyautogui.press("j")
    speak("Skipped backward.")

def set_volume(level):

    if level < 0 or level > 100:
        speak("Volume level should be between 0 and 100.")
        return

    pyautogui.press("m")  # Mute the video first to start fresh
    time.sleep(0.1)

    # Raise volume to 100, then decrease to desired level
    for _ in range(50):  # Pressing 'up' key repeatedly to ensure max volume
        pyautogui.press("up")
    for _ in range(50 - level):
        pyautogui.press("down")
    speak(f"Volume set to {level} percent.")

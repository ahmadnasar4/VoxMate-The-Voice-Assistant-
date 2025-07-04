import os
from core_utils import speak

# Mapping of app names to their executable commands
app_commands = {
    "command prompt": "cmd",
    "paint": "mspaint",
    "wps": "wps",
    "camera": "start microsoft.windows.camera:",
    "chrome": "chrome",
    "vs code": "code",
    "power bi": "pbidesktop",
    "whatsapp": "WhatsApp",
    "notepad": "notepad",
}

def open_app(app_name):

    command = app_commands.get(app_name.lower())
    if command:
        os.system(command)
        speak(f"{app_name} is now open.")
    else:
        speak(f"Sorry, I don't know how to open {app_name}.")

def close_app(app_name):

    command = app_commands.get(app_name.lower())
    if command:
        os.system(f"taskkill /f /im {command}.exe")
        speak(f"{app_name} is now closed.")
    else:
        speak(f"Sorry, I don't know how to close {app_name}.")

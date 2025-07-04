# 🦁 Leo: The Personal Voice Assistant

**Leo** is an advanced **Python-based AI voice assistant** designed to streamline tasks, automate workflows, and provide quick responses using voice commands. Built with a modular architecture, Leo offers a wide range of features including web searches, system management, real-time information, and personalized reminders—making it a powerful and customizable assistant for everyday use.

## ✨ Features

- **Web Searches**: Voice search on Google, YouTube, and Wikipedia.
- **System Commands**: Open/close applications, control system volume, shutdown system.
- **Real-Time Information**: Get current time, weather in Bhubaneswar, check internet speed.
- **Interactive Functions**: Play Rock-Paper-Scissors, manage personal notes and reminders.
- **Media Controls**: Control YouTube playback (play, pause, forward, volume control).
- **Advanced Capabilities**:
  - Hotword detection ("Leo").
  - Voice feedback on every interaction.
  - Google Translate integration.
  - Scheduling & reminders.
  - Optional GUI interface.

## 🗂️ Modules Overview

| Module              | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `core_utils.py`      | Core functions for speech, listening, hotword detection.                    |
| `greet.py`           | Manages greetings and conversational responses.                            |
| `web_search.py`      | Handles Google, YouTube, and Wikipedia search commands.                     |
| `temperature.py`     | Retrieves real-time weather for Bhubaneswar.                                |
| `app_management.py`  | Opens/closes system applications with voice commands.                       |
| `youtube_control.py` | Controls YouTube playback actions.                                          |
| `memory.py`          | Manages user-defined notes and recall functions.                           |
| `internet_speed.py`  | Checks internet download and upload speeds.                                |
| `game.py`            | Plays Rock-Paper-Scissors interactively with voice control.                 |
| `shutdown.py`        | Executes system shutdown command.                                           |

## 📦 Requirements

Install required Python packages with:

```bash
pip install pyttsx3 SpeechRecognition speedtest-cli requests wikipedia pywhatkit beautifulsoup4

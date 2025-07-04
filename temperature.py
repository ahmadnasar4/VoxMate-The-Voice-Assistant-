import requests
from bs4 import BeautifulSoup
from core_utils import speak


def check_temperature():
    url = "https://www.timeanddate.com/weather/india/bhubaneswar"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the temperature
        temp_element = soup.find("div", class_="h2")
        temp = temp_element.text.strip() if temp_element else "N/A"

        speak(f"The current temperature in Bhubaneswar is {temp}")
        print(f"The current temperature in Bhubaneswar is {temp}")
    except Exception as e:
        speak("Sorry, I couldn't retrieve the temperature.")
        print("Error:", e)



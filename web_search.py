from core_utils import speak
import wikipedia
import webbrowser
import pywhatkit as kit

def wikipedia_search(query):
    speak(f"Searching Wikipedia for {query}")
    print(f"Searching Wikipedia for {query}")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        print(results)
    except wikipedia.exceptions.PageError:
        speak("No matching page found on Wikipedia.")

def google_search(query):

    speak(f"Searching Google for {query}")
    print(f"Searching Google for {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak("Here are the Google search results.")
    print("Here are the Google search results.")


def youtube_search(query):
    """Search YouTube and open the results in a browser."""
    speak(f"Searching YouTube for {query}")
    print(f"Searching YouTube for {query}")
    kit.playonyt(query)
    speak("Playing the top YouTube result.")
    print("Playing the top YouTube result.")

def web_search(query, platform="wikipedia"):
    """Perform a web search on the specified platform."""
    if platform == "wikipedia":
        wikipedia_search(query)
    elif platform == "google":
        google_search(query)
    elif platform == "youtube":
        youtube_search(query)
    else:
        speak("Sorry, I can only search on Wikipedia, Google, or YouTube.")

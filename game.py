import random
from core_utils import speak

# Symbols for Rock, Paper, and Scissors
SYMBOLS = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌️"
}


def play_game():
    """Play a game of Rock-Paper-Scissors with the assistant."""
    choices = ["rock", "paper", "scissors"]
    assistant_choice = random.choice(choices)

    # Ask user for their choice
    speak("Let's play Rock-Paper-Scissors! Please say rock, paper, or scissors.")
    user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()

    # Validate user choice
    if user_choice not in choices:
        speak("Invalid choice. Please choose rock, paper, or scissors.")
        return

    # Display choices with symbols
    speak(
        f"You chose {user_choice} {SYMBOLS[user_choice]}, and I chose {assistant_choice} {SYMBOLS[assistant_choice]}.")

    # Determine the winner
    if user_choice == assistant_choice:
        speak("It's a tie!")
    elif (user_choice == "rock" and assistant_choice == "scissors") or \
            (user_choice == "paper" and assistant_choice == "rock") or \
            (user_choice == "scissors" and assistant_choice == "paper"):
        speak("Congratulations! You win!")
    else:
        speak("I win! Better luck next time.")

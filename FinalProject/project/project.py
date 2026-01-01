import re
import random
from INTENT_RESPONSE import INTENTS, RESPONSES
from rock_paper_scissor import play_rps
from guess_number import play_guess_number


def main():
    print("ChatMe: Hi! Do you want to chat or play a game?")

    while True:
        user_input = input("You: ")
        normalized = normalize_text(user_input)
        words = normalized.split()
        intent = detect_intent(words)

        if intent == "play":
            print("ChatMe:", generate_response("play"))
            game_choice = input("You: ").lower()
            print("ChatMe:", handle_game_selection(game_choice))
            continue

        response = generate_response(intent)
        print("ChatMe:", response)

        if should_exit(intent):
            break



def handle_game_selection(text):
    if "rock" in text:
        play_rps()
        return "That was fun! Want to play another game?"

    if "guess" in text:
        play_guess_number()
        return "Nice game! Want to play again?"

    return "Please choose Rock Paper Scissors or Guess the Number."



def normalize_text(text):
    normalised = re.sub(r'[^\w\s]', '', text.lower())
    normalised = re.sub(r'\s+', ' ', normalised).strip()
    return normalised


def detect_intent(words):
    for intent, keywords in INTENTS.items():
        for word in words:
            if word in keywords:
                return intent

    return 'unknown'


def generate_response(intent):
    return random.choice(RESPONSES.get(intent, RESPONSES["unknown"]))


def should_exit(intent):
    return intent == 'goodbye'



if __name__ == '__main__':
    main()

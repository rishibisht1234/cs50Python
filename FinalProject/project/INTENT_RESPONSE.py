INTENTS = {
    "greeting": {"hi", "hello", "hey"},
    "name": { "name", "who", "your" },
    "goodbye": {"bye", "exit", "quit", 'later'},
    "help": {"help"},
    "play": {"play", "game"},
    "yes": {"yes", "yeah", "yep", "sure"},
    "no": {"no", "nope", "nah"},
    "chat": {"talk", "chat"},
}

RESPONSES = {
    "greeting": [
        "Hello! 😊",
        "Hi there!",
        "Hey! How can I help you?"
    ],
    "name": [ "I'm ChatMe, a mini chatbot 🤖, Created by Rishi Bisht.",
             "You can call me ChatMe! I am created by Rishi Bisht" ],
    "help": [
        "I can chat with you or play games.",
        "Would you like to play a game?"
    ],
    "play": [
        "Sure! I have two games:",
        "Rock Paper Scissors and Guess the Number.",
        "Which one would you like to play?"
    ],
    "chat": [
        "Sure! Let's chat 😊",
        "I'm here to talk!"
    ],
    "yes": [
        "Great! What would you like to do?"
    ],
    "no": [
        "Alright! Let me know if you need anything."
    ],
    "goodbye": [
        "Goodbye! 👋",
        "See you soon!"
    ],
    "unknown": [
        "I'm not sure I understood that.",
        "Would you like to play a game or chat?"
    ]
}

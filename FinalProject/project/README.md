# ChatMe – A Rule-Based Python Chatbot with Games

#### Video Demo: [https://youtu.be/Mt48zeCvDXg](https://youtu.be/Mt48zeCvDXg)

## Description

ChatMe is a command-line based chatbot implemented in Python as a final project for CS50’s Introduction to Programming with Python (CS50P). The project demonstrates how a simple yet interactive chatbot can be built using rule-based logic, intent detection, and modular program design without relying on machine learning libraries.

The chatbot is capable of holding basic conversations with the user and can also launch small games on demand. Instead of trying to detect a large number of complex intents, the chatbot follows a guided interaction approach. It asks the user whether they want to chat or play a game and then responds accordingly. This design choice keeps the system simple, readable, and easy to extend.

The project focuses on clean control flow, separation of concerns, and testable logic, all of which align with the learning goals of CS50P.

---

## Features

- Text normalization to handle punctuation and inconsistent spacing
- Rule-based intent detection using keyword matching
- Interactive conversation loop
- Game integration:
  - Rock Paper Scissors
  - Guess the Number
- Modular code structure
- Automated tests using pytest

---

## File Structure

- `project.py`
  Contains the main chatbot logic. This includes input normalization, intent detection, response generation, game routing, and the main conversation loop.

- `INTENT_RESPONSE.py`
  Stores the `INTENTS` and `RESPONSES` dictionaries. This file separates conversational data from program logic, making the chatbot easier to maintain and extend.

- `rock_paper_scissor.py`
  Implements the Rock Paper Scissors game logic.

- `guess_number.py`
  Implements the Guess the Number game logic.

- `test_project.py`
  Contains unit tests for core logic functions such as text normalization, intent detection, and exit handling.

- `requirements.txt`
  Lists external dependencies required to run the project (pytest).

---

## How the Chatbot Works

1. The user enters input through the command line.
2. The input is normalized by converting it to lowercase, removing punctuation, and collapsing extra spaces.
3. The normalized input is split into words.
4. The chatbot detects the user’s intent by comparing words against predefined keyword sets.
5. If the intent is related to playing a game, the chatbot asks which game the user wants and launches it.
6. Otherwise, a predefined response is selected and displayed.
7. The conversation continues until the user enters a goodbye intent.

This rule-based approach makes the chatbot predictable, easy to test, and suitable for a learning-focused project.

---

## Testing

Automated tests are written using pytest and focus on deterministic logic only. Interactive components such as games and user input are intentionally excluded from testing.

To run the tests:

```bash
pytest

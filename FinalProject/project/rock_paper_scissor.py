import random

def play_rps():
    print("-"*10 + "Rock Paper Scissor Game" + "-"*10)
    choices = ['rock', 'paper', 'scissor']
    user_score = 0
    computer_score = 0
    rounds = 3

    for round in range(1, rounds + 1):
        print(f"\nRound {round}:")
        user_choice = input("Enter rock, paper, or scissor: ").lower()
        if user_choice not in choices:
            print("Invalid choice! Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissor') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissor' and computer_choice == 'paper'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game.")
    elif user_score < computer_score:
        print("Better luck next time! Computer won the game.")
    else:
        print("It's a tie game!")

if __name__ == '__main__':
    play_rps()

import random

def play_guess_number():
    print("-"*15 + 'Number Guess Game' + '-'*15 )
    print('''RULES: Guess a number between (0-10).
       If U Guessed it correct in 5 turns You win.''')
    Target = random.randint(0,10)
    wrong = 0
    while True:
        if wrong >=5:
            print('You Lose!!'+'\n'+ f'Correct Number is {Target}')
            break
        try:
            guess = int(input('Guess: '))
            if guess != Target:
                print('Wrong!')
                wrong += 1

            else:
                print('Correct!! YOU WON!!')
                break


        except Exception:
            print('Enter Valid number')
            continue

    print('_'*40)


if __name__ == '__main__':
    play_guess_number()

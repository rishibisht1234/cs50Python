import random

while True:
    level=input("Level: ")
    if not level.isdigit():
        continue
    level = int(level)

    if level>0:
        break

rn=random.randint(1,level)

while True:
    guess=input('Guess: ')

    if not guess.isdigit():
        continue

    guess=int(guess)

    if guess<=0:
        continue

    if guess==rn:
        print('Just right!')
        break

    elif guess>rn:
        print('Too large!')
    elif guess<rn:
        print('Too small!')

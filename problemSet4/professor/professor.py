import random

def get_level():
    while True:
        try:
            n=int(input('Level: '))
            if n in [1,2,3]:
                return n
        except Exception:
            continue

def generate_integer(level):
    if level not in [1,2,3]:
        raise ValueError()
    if level==1:
        l,u=(0,9)
    elif level==2:
        l,u=(10,99)
    elif level==3:
        l,u=(100,999)
    x=random.randint(l,u)
    return x


def main():
    level=get_level()
    score=0
    for _ in range(10):
        x,y=(generate_integer(level),generate_integer(level))
        E=0
        while True:
            try:
                ans=int(input(f'{x} + {y} = '))
                if ans!=x+y:
                    raise Exception()
                score+=1
                break
            except Exception:
                print('EEE')
                E+=1
                if E==3:
                    print(f'{x} + {y} = {x+y}')
                    break
                else:
                    continue
    print(f'Score: {score}')


if __name__ == "__main__":
    main()


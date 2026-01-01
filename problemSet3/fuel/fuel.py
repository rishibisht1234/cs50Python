def convert(fraction):
    x,y=fraction.split('/')

    try:
        x = int(x)
        y = int(y)
    except Exception:
        raise ValueError()

    if x>y or x<0 or y<0:
        raise ValueError()
    if y==0:
        raise ZeroDivisionError()

    percentage=round((x/y)*100)

    return percentage



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    fraction = input("Fraction: ")
    percentage=convert(fraction)
    print(gauge(percentage))


if __name__ == "__main__":
    main()

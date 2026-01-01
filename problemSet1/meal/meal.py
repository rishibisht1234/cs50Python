def main():
    time=input("What time is it? ")
    value=convert(time)
    print(meal(value))


def meal(value):
    if 7<=value<=8:
        return "breakfast time"
    elif 13<=value<=14:
        return "lunch time"
    elif 18<=value<=19:
        return "dinner time"
    else:
        return ""


def convert(time):
    time=time.split(":")
    hours=float(time[0])
    minutes=float(time[1])
    hours+=float(minutes/60)
    return hours



if __name__ == "__main__":
    main()

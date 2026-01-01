def value(greeting):
    greeting=greeting.strip().lower()
    if greeting[0:5]=="hello":
        out="$0"
    elif greeting and greeting[0]=="h":
        out="$20"
    else:
        out="$100"
    return out


def main():
    greeting=input("Greeting: ")
    print(out)


if __name__ == "__main__":
    main()

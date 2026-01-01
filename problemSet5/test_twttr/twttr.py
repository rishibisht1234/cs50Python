def main():
    str=input("Input: ")
    ans=shorten(str)
    print(f"Output: {ans}")


def shorten(str):
    vowels=["a","e","i","o","u"]
    ans=''.join([char for char in str if char.lower() not in vowels])
    return ans


if __name__=='__main__':
    main()


import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    m = re.findall(r"\bum\b", s, re.IGNORECASE)
    print(m)
    if m:
        return len(m)
    return 0


if __name__ == "__main__":
    main()

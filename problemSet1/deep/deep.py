def reply(q):
    q=q.lower()
    if (("42" in q) or ("forty-two" in q) or ("forty two" in q)):
        return "Yes"
    else:
        return "No"

def main():
    q=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    print(reply(q))

main()

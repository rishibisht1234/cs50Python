def coke():
    due=50
    while(due>0):
        coin=int(input("insert coin: " ))
        while coin!=5 and coin!=10 and coin!=25:
            print(f"Amount Due: {due}")
            coin=int(input("insert the right coins : "))
        due=due-coin
        if due>0:
            print(f"Amount Due: {due}")

    print(f"Change owed: {abs(due)}")


coke()









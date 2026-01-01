import validators

def main():
    email=input("What's your email address? ")
    isvalid=validators.email(email)

    if isvalid:
        print('Valid')
    else:
        print("Invalid")

if __name__=='__main__':
    main()

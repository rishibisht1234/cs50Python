def snake_case(camelCase):
    str=''
    for ch in camelCase:
        if ch.isupper():
            str+='_' + ch.lower()
        else:
            str+=ch
    return str

def main():
    a=input("camelCase : ")
    ans=snake_case(a)
    print(f"snake_case : {ans}")

main()

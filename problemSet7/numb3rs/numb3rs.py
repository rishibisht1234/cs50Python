import re

# def validate(s):
#     try:
#         s = s.split('.')
#         s = list( map(lambda x: int(x),s) )

#         if (len(s) != 4):
#             return False

#         if s[0] in range(0,256) and s[1] in range(0,256) and s[2] in range(0,256):
#             return True

#         return False

#     except Exception:
#         return False

def validate(ip):
    if re.search(r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$", ip):
        return True
    return False

def main():
    print(validate(input("IPv4 Address: ")))


if __name__=='__main__':
    main()



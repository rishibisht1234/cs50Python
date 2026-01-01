import sys
from pyfiglet import Figlet
# figlet.getFonts()
# figlet.setFont(font=f)
# print(figlet.renderText(s))

f=Figlet()



if not (len(sys.argv) ==1 or  len(sys.argv)==3):
    sys.exit('Invalid Usage')


if len(sys.argv)==3:
    if sys.argv[1] not in ['-f' , '--font'] or sys.argv[2] not in f.getFonts():
        sys.exit('Invalid Usage')
    string=input("Input: ")
    fo=sys.argv[2]
    f.setFont(font=fo)
    print(f.renderText(string))

else:
    string=input("Input: ")

    print(f.renderText(string))

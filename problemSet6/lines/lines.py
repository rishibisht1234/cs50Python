import sys

if len(sys.argv)==1:
    sys.exit('Too few command-line arguments')
if len(sys.argv)>2:
    sys.exit('Too many command-line arguments')

fname=sys.argv[1]
# print(fname.endswith(".py"))

if not fname.endswith('.py'):
    sys.exit('Not a python file')


try:
    with open(fname,'r') as f:
        lines=f.readlines()
        # excluding comment
        # lines=list(filter(lambda x:))
        lines=list(filter(lambda x:x.strip() and (not x.lstrip().startswith('#')),lines))
        print(len(lines))
except FileNotFoundError:
    sys.exit('File does not exist')

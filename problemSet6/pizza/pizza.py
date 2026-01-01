import sys
from tabulate import tabulate


if len(sys.argv)<2:
    sys.exit('Too few command-line arguments')
if len(sys.argv)>2:
    sys.exit('Too many command-line arguments')

csv_name=sys.argv[1]

if not csv_name.endswith('.csv'):
    sys.exit('Not a CSV file')

try:
    with open(csv_name,'r') as f:
        lines=f.readlines()
        for index,line in enumerate(lines):
            lines[index]=line.strip().split(',')
        # print(lines)
        print(tabulate(lines,headers='firstrow',tablefmt='grid'))

except FileNotFoundError:
    sys.exit('File does not exist')



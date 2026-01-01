import sys
import inflect
from datetime import date, timedelta
import re

p=inflect.engine()

def date_parser(date_str):
    try:
        d = date.fromisoformat(date_str)
        # print('type of date is :',type(d))
        if date.today()<d:
            raise ValueError()
        return d
    except ValueError:
        sys.exit('Invalid date')


def calculate(dob):
    today=date.today()
    n=today-dob
    minutes=int(n.total_seconds()/60)
    return p.number_to_words(minutes).capitalize().replace(' and ',' ') + ' minutes'


def main():
    DOB = input('Date of Birth: ')
    DOB = date_parser(DOB)
    print(calculate(DOB))




if __name__ == "__main__":
    main()


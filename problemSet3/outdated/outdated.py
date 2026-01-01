# input: 9/8/1636 or September 8, 1636
# output: YYYY-MM-DD
months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def initial_check(date): #required
    if '/' in date:
        return True
    if ',' in date:
        return True
    return False

def is_in_range(year,month,day): # required
    if day>31 or day<1:
        return False
    if month>12 or month<1:
        return False
    if year>9999:
        return False
    return True

def type_check(year,month,day):
    if year.isdigit() and day.isdigit():
        if month.isdigit():
            return (True,True)
        else:
            return (True,False)
    return (False,False)


# main

while True:
    inputed_date=input('Date: ')
    if not initial_check(inputed_date):
        continue

    if '/' in inputed_date:
        date=inputed_date.strip().split('/')
        if len(date) != 3:
            continue
        month,day,year=(date[0],date[1],date[2])

        year_date_check,month_check=type_check(year,month,day)
        if not (year_date_check and month_check):
            continue
        month,day,year=(int(month),int(day), int(year))
        if not is_in_range(year,month,day):
            continue

        print(f"{year}-{month:02}-{day:02}")
        break

    if ',' in inputed_date:
        date=inputed_date.strip().replace(',','').split()
        if len(date)!=3:
            continue
        month,day,year=(date[0],date[1],date[2])
        year_date_check,month_check=type_check(year,month,day)
        if not (year_date_check and not month_check):
            continue
        day,year=(int(day), int(year))
        if month in months:
            month=months.index(month)+1
            if not is_in_range(year,month,day):
                continue
            print(f"{year}-{month:02}-{day:02}")
            break










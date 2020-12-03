import datetime

def check_sunday(date):
    if date.weekday() == 6:
        return True

start = datetime.date(1901, 1, 1)

counter = 0

while start != datetime.date(2001, 1, 1):
    if check_sunday(start) == True:
        counter =+ 1
    if 
    start += datetime.timedelta(months)
    print(start)

print("\nThe amount of Sundays that fall on the first of the month during the 20th century is: ", counter)
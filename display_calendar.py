# This module display calendar

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

print(calendar.month(year, month, day))

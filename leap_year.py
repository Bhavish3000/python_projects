def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:  
            return True
    else:
        return False

entered_year = int(input("Enter the year: "))  # Convert input to an integer
print(is_leap_year(year=entered_year))

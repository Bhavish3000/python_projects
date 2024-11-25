def life_in_weeks(age):
    weeeks_in_year = 52
    
    weeks_left = ( 90- age)*weeeks_in_year   #max age is 90 years
    print(f"You have {weeks_left} weeks left.")
    
life_in_weeks(23)
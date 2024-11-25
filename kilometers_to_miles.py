""" This module converts kilometers to miles
"""
kilometers = float(input("Enter kilometers: "))
# Conversion factor: 1 kilometer = 0.621371 miles
CONVERSION_FACTOR = 0.621371
miles = kilometers * CONVERSION_FACTOR

print(f"{kilometers} kilometers is equal to {miles} miles")

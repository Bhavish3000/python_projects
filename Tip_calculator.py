"""This module calculates the Tip's
"""
print("Welcome to the tip calculator!")
Total = int(input("What was the total bill?"))
tip = int(input("How much tip would like to give? 10, 12, or 15?"))
split = int(input("How many people to split the bill?"))
calculation = ((100 / tip) + Total) / split

print(f"Each persion should pay: ${calculation}")
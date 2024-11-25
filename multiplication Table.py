"""_This module prints multiplication Table
"""

num= int(input("Displaying the multiplication of: "))
RANGE = int(input("Enter the upper limit: "))
for i in range (1, RANGE+1):
    print(f"{num} * {i} = {num*i}")
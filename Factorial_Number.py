"""_This module prints the Factorial of the numbers
"""
num= int(input("Enter the number:"))
Factorial =1
if num < 0:
    print("Enter positive number, Factorial doesn't exsist for Negative Number")
elif num ==0:
    print("Factorial number of 0 is 1")
else:
    for i in range (1, num+1):
        Factorial = Factorial*i
print(f"Factorial of the {num} is {Factorial}")

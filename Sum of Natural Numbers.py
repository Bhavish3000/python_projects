"""_This module prints the SUM of Natural Numbers
"""
limit = int(input("Enter the limit:"))
# Initialize the SUM
SUM= 0
# Use a for loop to calculate the SUM of natural numbers
for i in range(1, limit+1):
    SUM += i
    # Print the sum

print(f"SUM of Natural Numbers {SUM}")

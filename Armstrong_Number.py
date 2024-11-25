"""_This module checks for the armstrong number
"""

number= int(input("Enter the number:"))
# Calculate the number of digits in num
STRING_CONVERTED=   str(number)
LENGTH_NUMBER= len(STRING_CONVERTED)
# Initialize variables
temp_number= number
sum_0f_Square_Digit= 0
# Calculate the sum of digits raised to the power of num_digits
while temp_number > 0:
    digit= temp_number%10
    sum_0f_Square_Digit += digit**LENGTH_NUMBER
    temp_number//=10
# Calculate the sum of digits raised to the power of num_digits
if sum_0f_Square_Digit == number:
    print(f"{number} is an Armstrong Number")
else:
    print(f"{number} is not an Armstrong Number")

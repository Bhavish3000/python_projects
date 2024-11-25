"""This module generates password
"""
import random

characters= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 'z']
numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters=  ['!', '@', '#', '$', '%', '^', '&', '*']

password = []
char_len = int(input("Enter char length:"))
for i in range (0, char_len):
    password.append(random.choice(characters))
num_len= int(input("Enter number length:"))
for i in range(0, num_len):
    password.append(random.choice(numbers))
spe_len= int(input("Enter specialchar_len:"))
for i in range(0, spe_len):
    password.append(random.choice(special_characters))
random.shuffle(password)

PASS_KEY= ""
for i in password:
    PASS_KEY += i

print(PASS_KEY)

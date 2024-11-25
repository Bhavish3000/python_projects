""" This module swap two variables
"""
a = int(input("a = "))  # Input two variables
b = int(input("b = 5"))
# Swap the values using a temporary variable
temp = a
a = b
b = temp
# Display the swapped values
print(f"a = {a}")
print(f"b = {b}")

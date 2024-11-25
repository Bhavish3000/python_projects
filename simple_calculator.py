"""_This module is an Simple calculator
"""
def add(x, y):
    """_This function adds two parameters_

    Args:
        x (_float_): _Takes the input as float_
        y (_float_): _Takes the input as float_
    """
    return x+y

def sub(x, y):
    """_This function subtracts two parameters

    Args:
        x (_float_): _Takes the input as float_
        y (_float_): _Takes the input as float_
    """
    return x-y
def mux(x, y):
    """_This function multiplicates two parameters

    Args:
        x (_float_): Takes the input as float_
        y (_float_): Takes the input as float_
    """
    return x*y
def div(x, y):
    """_This function divides two parameters

    Args:
        x (_float_): Takes the input as float_
        y (_float_): Takes the input as float_
    """
    return x/y

print("Select operation.")
print("+.Add")
print("-.Subtract")
print("*.Multiply")
print("/.Divide")

while True:
    choice = input(" Enter the operator (+, -, *, / )")
    # check if choice is one of the four options
    if choice in ('+', '-', '*', '/'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '+':
            print (f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '-':
            print (f"{num1} - {num2} = {sub(num1, num2)}")
        elif choice == '*':
            print (f"{num1} * {num2} = {mux(num1, num2)}")
        elif choice == '/':
            print (f"{num1} / {num2} = {div(num1, num2)}")
        next_calculation = input("Let's do next calculation? (yes/no):")
        if next_calculation == 'no':
            break
    else:
        print("Invalide input")

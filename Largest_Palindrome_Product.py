"""_Finding the largest palindrome made from the product of two 
-digit numbers._"""

def is_palindrome (n):
    """_Checking the number is palindrome_

    Args:
        n (_int_)
    """
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    """_Find the largest palindrome made from the product of two 3-digit numbers._"""

    max_palindrome = 0
    factors = (0,0)
    # Iterate through all products of two 3-digit numbers
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product <= max_palindrome:
                break
            if is_palindrome(product):
                max_palindrome = product
                factors = (i,j)
    return max_palindrome, factors

largest_palindrome, (factor1, factor2) = largest_palindrome_product()
print(f"The largest palindrome made from the product of two 3-digit numbers is {largest_palindrome} = {factor1} * {factor2}.")
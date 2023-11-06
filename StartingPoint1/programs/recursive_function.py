# An example of a recursive function to
# find the factorial of a number
import sys


def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = int(input('Enter a number to find the factorial '))
print("The factorial of", num, "is", calc_factorial(num))





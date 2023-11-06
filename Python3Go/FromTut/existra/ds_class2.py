# easy method
# import math
# from math import factorial
import sys


#
# print(factorial(123))

# hard way

def de_fact(any_number):
    if any_number == 1:
        return 1
    else:
        return (any_number * (de_fact (any_number - 1)))



de_fact(1)
number = int (input ('Enter a number to calculate factorial : '))
print ('The result of fcu***g number', number, 'factorial is', de_fact (number))




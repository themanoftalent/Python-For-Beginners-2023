# import math
# from math import factorial
# import sys
# sys.setrecursionlimit(1500)
'''

It is a guard against a stack overflow, yes. Python (or rather, the CPython implementation) doesn't optimize tail recursion, 
and unbridled recursion causes stack overflows. You can change the recursion limit with sys.setrecursionlimit, but doing 
so is dangerous -- the standard limit is a little conservative, but Python stackframes can be quite big.
Python isn't a functional language and tail recursion is not a particularly efficient technique. Rewriting the algorithm 
iteratively, if possible, is generally a better idea.
'''

# #print (factorial (100))  #this is the shortes way
# print(factorial(100**10)) #OverflowError: factorial() argument should not exceed 9223372036854775807
# print(factorial(int(input('Enter a number : ')))) #here we enter a number tocalculate the factorial
# #some other ways are to define a func
# -------------------------------------------------

# An example of a recursive function to
# find the factorial of a number

def needFac(x):
    if x == 1:
        return 1
    else:
        return (x * needFac (x - 1))


number1 = int (input ('Enter a number '))
print ('The factorial of ', number1, 'is', needFac (number1))


# def calc_factorial(number):
#     """This is a recursive function
#     to find the factorial of an integer"""
#
#     if number == 1:
#         return 1
#     else:
#         return (number * calc_factorial(number-1))
#
# num = int(input('Enter a number to calculate factorial : '))
# print("The factorial of", num, "is", calc_factorial(num))
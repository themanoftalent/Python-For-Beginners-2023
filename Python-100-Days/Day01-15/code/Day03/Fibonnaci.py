#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
# 

numberOfterms = int(input("How many terms? "))

n1, n2 = 0, 1
CountNumbers = 0

if numberOfterms <= 0:
    print("Greater than zero, positive number")

elif numberOfterms == 1:
    print('Value is zero', 0)

# elif numberOfterms==2:
#     print('Fibonnaci two equals {} and {}: '.format(0,1))

else:
    print("Fibonacci sequence:")
    while CountNumbers < numberOfterms:
        print(n1)
        FiboNumber = n1 + n2

        n1 = n2
        n2 = FiboNumber
        CountNumbers += 1

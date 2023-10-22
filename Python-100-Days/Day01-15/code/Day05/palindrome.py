#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

'''
Palindrome are the kind of strings which are same from left or right whichever way you read them.
Example “madam”. In this example we will take the word as input from the user and say if it is palindrome or not.
'''

texting = input("Please enter a string: ")
ztext = texting[::-1]

if texting == ztext:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

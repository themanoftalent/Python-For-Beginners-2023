##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################

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

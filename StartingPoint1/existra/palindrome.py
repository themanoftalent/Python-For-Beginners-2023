'''
Palindrome are the kind of strings which are same from left or right whichever way you read them.
Example “madam”. In this example we will take the word as input from the user and say if it is palindrome or not.
'''

s = input ("Please enter a string: ")
z = s[::-1]
if s == z:
    print ("The string is a palindrome")
else:
    print ("The string is not a palindrome")

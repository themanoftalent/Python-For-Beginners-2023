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


# Accessing Values in Strings
variable1 = "akif!"
variable2 = "Software Testing"
print('=======' * 3)
print("variable1[0] (akif) :", variable1[0])
print("variable2[1:5] (Software Testing):", variable2[1:5])
print('=======' * 3)

# Some more examples
x = "Hello World!"
print(x[:6])
print(x[0:6] + "akif")

# Python String replace() Method
oldstring = 'I like akif'
newstring = oldstring.replace('like', 'love')
print(newstring)
# Changing upper and lower case strings
string = "python with akif"
print('in uppercase ', string.upper())
string = "python with akif"
print('Caps ', string.capitalize())
string = "PYTHON with akif"
print('lowercase ', string.lower())
# Using "join" function for the string
print("_".join("Python"))
print('-'.join(variable1))  # variable1 is akif

# Reversing String
string = "123456789"
print(''.join(reversed(string)))
# Split Strings
word = "akif is a great man"
print(word.split(' '))
word = "akif is a coder"
print(word.split('r'))
var3 = "akif replace"
var3.replace("akif", "The great man ever")
print(var3)
var4 = "akif"
var4 = var4.replace("akif", "Python coding")
print(var4)

print('+++++++++++++++++++++++++++++')
name = 'Swarming man'
if name.startswith('Sw'):
    print('Yes it starts with sw')
else:
    print('No it is not ')
if 'a' in name:
    print('Yes, it contains the string "a"')
if name.find('war'):
    print('Yes, it contains the string "war"')

if name.find('min') != -1:
    print('what the hack it contains ming')
if name.find('i'):
    print(repr(name))


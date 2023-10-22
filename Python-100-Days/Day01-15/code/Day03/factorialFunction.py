#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

def fack(n):
    if n<=1:
        return n
    
    if n==2:
        return n
    
    else:
        return n*fack(n-1)
    
    
print(fack(7))



# def fack(n):
#     if n==1 or n==2:
#         return n
#
#     else:
#         return n*fack(n-1)
#
#
# print(fack(5))
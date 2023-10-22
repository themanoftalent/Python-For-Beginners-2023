#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

A = [1,3,5,7,9]
B = [2,4,6,8,10]

Kartezyen =[(a, b) for a in A for b in B]
print(Kartezyen)
print('====='*21)

toplama=[(a+ b) for a in A for b in B]
print(toplama)
print('====='*21)
cikarma=[(a- b) for a in A for b in B]
print(cikarma)
print('====='*21)
carpma=[(a* b) for a in A for b in B]
print(carpma)

print('====='*21)
bolme=[(a/ b) for a in A for b in B if a//4==0 and b==4]
print(bolme)

#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

def cm(feet=0,inches=0):
    '''Writing some doc and importing mymodule'''



    inches_cm=inches*2.54
    feet_cm=feet*12*2.54
   


    print(inches_cm+feet_cm)


cm(feet=5)

print(cm.__doc__)

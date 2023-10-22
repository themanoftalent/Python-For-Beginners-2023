#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import random
import os
import sys

try:
    aNum = int (input ('Enter a number :'))

except ValueError:

    if aNum > 0 and aNum < 100:
        print ('Correct', aNum)
    else:
        print ('Try again')

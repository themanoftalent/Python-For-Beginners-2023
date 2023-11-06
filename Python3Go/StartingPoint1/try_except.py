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

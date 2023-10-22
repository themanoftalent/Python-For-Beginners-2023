
#  !/usr/bin/python
#  Copyright (c) akifciftci 2019. Aim to help new beginner to try hard and learn more.
#

from random import randint

face = randint(1, 6)
if face == 1:
    result = 'BIR'
elif face == 2:
    result = 'IKI'
elif face == 3:
    result = 'UC'
elif face == 4:
    result = 'DORT'
elif face == 5:
    result = 'BES'
else:
    result = 'ALTI'
print(result)

#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import os
from pathlib import Path
filepath=Path("/Users/darwin/Desktop/wadata.txt")

print(filepath.name)
print(filepath.suffix)
print(filepath.parent)
print(filepath.open)
print(filepath.stem)

if not filepath.exists():
    print('File does not exist, you moron!')
else:
    print('Welcome to file')
if filepath.exists():
    with open(filepath,'a+') as f:
        for number in range(1,10001):
            f.write(' Help man, we are here,  i am gonna fuck all of you thousand times yeah number -'+str(number))

with open(filepath,'r') as f:
    for lines in f.readlines():
        print(lines,'\n')

# os.remove(filepath)







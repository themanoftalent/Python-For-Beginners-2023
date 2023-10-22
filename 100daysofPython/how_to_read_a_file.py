#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import os
import pathlib
from pathlib import Path


print(os.getcwd())

# dirName = '/Users/darwin/tempDir2/temp2/temp'
# print(os.mkdir(dirName))

mypath=Path('/Users/***/tempDir2/temp2/temp/newfile.txt')

try:
    with open(mypath,'w') as f:
        for lines in range(10001):
            f.write(' Canavar '+ str(lines)+ '\n')
except FileNotFoundError():
    print('what the fuck')

try:
    with open(mypath,'r') as f:
        print(f.read())

except: FileNotFoundError()

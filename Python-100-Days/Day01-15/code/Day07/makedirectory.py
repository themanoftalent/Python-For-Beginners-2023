#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import os
import pathlib
from pathlib import Path


def main():
    dirName=Path('/Users/***/Desktop/tempDir')
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
    print("Directory " , dirName ,  " already exists")
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:
        print("Directory " , dirName ,  " already exists")
        dirName=Path('/Users/***/Desktop/tempDir')

        os.mkdir(dirName)
        print("Directory ", dirName ,  " Created ")

        print("Directory " , dirName ,  " already exists")


        if not os.path.exists(dirName):
            os.makedirs(dirName)
            print("Directory " , dirName ,  " Created ")
            print("Directory " , dirName ,  " already exists")    

if __name__ == '__main__':
    main()
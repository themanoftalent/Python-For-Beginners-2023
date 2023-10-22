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
#

import os
from pathlib import Path
file_pathing=Path('/Users/darwin/Downloads/ted.txt')

print(file_pathing.name)
print(file_pathing.stem)
print(file_pathing.suffixes)
print(file_pathing.parent)
print(file_pathing.is_dir())

if not file_pathing.exists():
    with open(file_pathing,'w') as f:
        f.write('Hey there')
else:
    with open(file_pathing,'r') as f:
        nopesa=f.read()
        print(nopesa)


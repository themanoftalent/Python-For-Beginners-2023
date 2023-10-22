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

import re

def main():
    fh = open('raven.txt')
    # Compiling a regex for loops like this will perform better than compiling it every time
    # It also lets us use arguments such as "ignorecase"
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub('###', line), end='')

if __name__ == "__main__": main()

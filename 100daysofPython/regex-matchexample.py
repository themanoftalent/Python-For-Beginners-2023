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
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group())

if __name__ == "__main__": main()

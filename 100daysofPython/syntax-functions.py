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

def main():
    func(1)
    func()
    func(5)


def func(a = 7):
    for i in range(a, 10):
        print(i, end = " ")
    print()

if __name__ == "__main__": main()


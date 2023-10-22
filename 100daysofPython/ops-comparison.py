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
    print("This is the ops.py file.")

    #Operator examples
    print("5 < 6 = {}".format(5 < 6))
    print("6 < 5 = {}".format(6 < 5))

    print("5 <= 6 = {}".format(5 <= 6))
    print("5 <= 5 = {}".format(5 <= 5))

    print("5 == 5 = {}".format(5 == 5))
    print("5 == 6 = {}".format(5 == 6))

    print("6 != 6 = {}".format(6 != 6))
    print("6 != 7 = {}".format(6 != 7))

    x, y = 5, 6
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("id(x) = {}".format(id(x)))
    print("id(y) = {}".format(id(y)))
    print("x is y = {}".format(x is y))
    print("x is not y = {}".format(x is not y))
    print("Setting y to 5...")
    y = 5
    print("y = {}".format(y))
    print("id(y) = {}".format(id(y)))
    print("x is y = {}".format(x is y))
    print()
    x, y = [5], [5]
    print("x, y = [5], [5]")
    print("x == y = {}".format(x == y))
    print("x is y = {}".format(x is y))

if __name__ == "__main__": main()

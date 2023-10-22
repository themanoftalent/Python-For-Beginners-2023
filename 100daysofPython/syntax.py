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
    a = 7
    print(type(a), a)
    print("This is the syntax.py file.")

    a, b = 0, 1
    a, b = 1, 1
    a, b = 2, 1

    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")


    # Tertiary conditional form
    s = "Less than" if a < b else "Not less than"
    print(s)



if __name__ == "__main__": main()

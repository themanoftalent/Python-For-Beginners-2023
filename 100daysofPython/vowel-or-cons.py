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
    x=input("Enter a alphabet=")
    try:
     y=['a','e','i','o','u','A','E','I','O','U']
     if(str(x) in y):
        print(x+" is vowel")
     else:
        print(x+" is consonant")
    except:
        print("invalid entry")
if __name__ == '__main__':
    main()

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

try:
    def reverse(s):
        return s[::-1]
    def isPalindrome(s):
        rev = reverse(s)
        if (s == rev):
            return True
        return False
    s=str(input("enter digit"))
    ans = isPalindrome(s)
    if(int(s)>1000):
        print("enter less than 1000")
    elif ans == 1:
        print("Yes")
    else:
        print("No")
except:
    print("Invalid entry")

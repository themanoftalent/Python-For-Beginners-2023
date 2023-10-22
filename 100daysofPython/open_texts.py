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

f:
    f_contents = f.read ()
    size_to_read = 100
    nano_to_read = 0

    while len (f_contents) > nano_to_read:
        print (f_contents)
        f_contents = f.read (size_to_read)

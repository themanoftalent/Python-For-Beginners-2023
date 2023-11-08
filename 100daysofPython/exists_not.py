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



import os

# Your path here e.g. "C:\Program Files\text.txt"
# For access purposes: "C:\\Program Files\\text.txt"
if os.path.exists("~/Desktop/bura/points.kml"):
    print ("File found!")
else:
    print ("File not found!")

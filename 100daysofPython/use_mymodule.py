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

# Filename: using_mymodule.py
# Description: This script is used to test
# the module I wrote in mymodule.py

import mymodule

mymodule.sayHello() # using . to set which module to use
print mymodule.version 

### Note: if using from mymodule import *, then we could 
### use every function and varible without '.'

#! /usr/bin/python
# Filename: str_method.py
# Description: basic function of str

name = "deercoder"

if name.startswith('de'):
    print 'string is startwith de'
if 'a' in name:
    print 'a is in the string'
if name.find('code') != -1:
    print 'found \'code\' in the string'

delimiter = "_*_"
mylist =['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)

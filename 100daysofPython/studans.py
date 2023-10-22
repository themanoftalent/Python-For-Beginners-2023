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

n = int(input("Enter the number of students:"))
data = {} # here we will store the data
languages = ('English', 'Maths', 'History') #all languages

for i in range(0, n): #for the n number of students
    name = input('Enter the name of the student %d: ' % (i + 1)) #Get the name of the student
    marks = []
    for x in languages:
        marks.append(int(input('Enter marks of %s: ' % x))) #Get the marks for  languages
    data[name] = marks
for x, y in data.iteritems():
    total =  sum(y)
    print("%s 's  total marks %d" % (x, total))
    if total < 120:
        print("%s failed :(" % x)
    else:
        print("%s passed :)" % x)

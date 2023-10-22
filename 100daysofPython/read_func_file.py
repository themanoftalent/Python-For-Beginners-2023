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
#

try:
    def writing():
        with open('writes.txt', 'a') as f:
            for num in range(100):
                f.write('Whatman ' + str(num) + '\n')

except:
    Exception
    print('File not found')

try:
    def readFile():
        with open('writes.txt', 'r')  as f:
            for lines in f.readlines():
                #when make readline it reads letter by letter
                print(lines)

except:
    Exception
    print('Fuck you')






writing()

readFile()

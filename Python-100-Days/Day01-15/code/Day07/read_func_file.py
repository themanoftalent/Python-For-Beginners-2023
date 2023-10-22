#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
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

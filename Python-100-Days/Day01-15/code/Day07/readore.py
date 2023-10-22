#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#
#

file = open('testfile.txt', 'r+')

file.write('Hello World')
file.write('This is our new text file')
file.write(' and this is another line.')
file.write('Why? Because we can.')
file.write('This is a test')
file.write('To add more lines.')

# file.close()


print(file.read())


print("===="*23)

#
# Let's show some examples
# To open a text file, use:
# fh = open("hello.txt", "r")
#
# To read a text file, use:
# fh = open("hello.txt","r")
# print fh.read()
#
# To read one line at a time, use:
# fh = open("hello".txt", "r")
# print fh.readline()
#
# To read a list of lines use:
# fh = open("hello.txt.", "r")
# print fh.readlines()
#
# To write to a file, use:
# fh = open("hello.txt","w")
# write("Hello World")
# fh.close()
#
# To write to a file, use:
# fh = open("hello.txt", "w")
# lines_of_text = ["a line of text", "another line of text", "a third line"]
# fh.writelines(lines_of_text)
# fh.close()
#
# To append to file, use:
# fh = open("Hello.txt", "a")
# write("Hello World again")
# fh.close()
#
# To close a file, use
# fh = open("hello.txt", "r")
# print fh.read()
# fh.close()

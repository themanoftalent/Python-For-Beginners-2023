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

def main():
    f= open("gpedit.txt","w+")
    f=open("gpedit.txt","a+")
    for i in range(10):
         f.write("This is line %d\r\n" % (i+1))
    f.close()
    #Open the file back and read the contents
    f=open("gpedit.txt", "r")
    if f.mode == 'r':
       contents =f.read()
    print (contents)
if __name__== "__main__":
  main()

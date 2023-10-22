#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
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
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#
#


# this is very basic of reading a text
f = open('howfast.txt')
readtext = f.read()
print(readtext)
f.close

print("========" * 24)

# if you down want to close the file there is a better way of this lets try
with open('howfast.txt') as fobj:
    # or we could make like
    # readme=fobj.read()
    # yet print is a shortway
    print(fobj.read())

# what if teh file is not exist
# lets give a shot
print("========" * 24)

try:
    with open('afilenotexist.txt') as nofile:
        text = nofile.read()
except:
    FileNotFoundError
text = 'File not exist'
#or we could write that None
#like text=None
#to surround with try except command option + t

print(text)

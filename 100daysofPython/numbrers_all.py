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
print(list(range(0,100,20)))
print("=================================")

for item in [0,20,40,60][:3]:
    print(item)

print("=================================")
ids=['B3','\nB4','\nB5','\nB6']

with open('ids.txt','w') as f:

    for item in ids:
        f.write(item)

with open('ids.txt','r') as fs:
   line=fs.read()
   for line in ids:
       print(line)
#=================================

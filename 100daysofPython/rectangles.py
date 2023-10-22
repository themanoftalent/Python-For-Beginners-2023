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

f = open("rectangles.txt")
for line in f:
    if line == "```\n":
        print "```"
    else:
        points = line.replace("\n", "").split(",")
        points = map(int, points)
        firstRec = points[0:4]
        secdRec = points[4:]
        firstRec = xrange(firstRec[0], firstRec[-1]+1)
        secdRec = xrange(secdRec[0], secdRec[-1]+1)

        if len(set(firstRec) & set(secdRec)) < 2:
            print "None"
        else:
            setList = []
            for i in set(firstRec) & set(secdRec):
                setList.append(i)
            print str(setList[0])+","+ str(setList[0])+","+ str(setList[-1])+","+ str(setList[-1])

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


class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1 
        print ("My name is %s" % self.name)

    def __del__(self):
        Person.population -= 1
        print ("%s say goodbye" % self.name)
        if Person.population == 0:
            print( "I am the last one")
        else:
            print ("the population is ", Person.population)

    def sayHi(self):
        print ("Hi, I am %s" % self.name)
        print ("Population is %d" % Person.population)
        
    def howmany(self):
        print ("The current population is ", Person.population)


test1 = Person("Ahmet")
test1.sayHi()
test1.howmany()

test2 = Person("Mehmet")
test2.sayHi()
test2.howmany()

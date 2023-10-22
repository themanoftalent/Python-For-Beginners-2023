
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#


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

#! /usr/bin/python
# Filename object.python
# Description: user of object variable and class variables

class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1 # Note: must using Person.population
        print "My name is %s" % self.name
    def __del__(self):
        Person.population -= 1
        print "%s say goodbye" % self.name
        if Person.population == 0:
            print "I am the last one"
        else:
            print "the population is ", Person.population
    def sayHi(self):
        print "Hi, I am %s" % self.name
        print "Population is %d" % Person.population
    def howmany(self):
        print "The current population is ", Person.population


test1 = Person("test1")
test1.sayHi()
test1.howmany()

test2 = Person("test2")
test2.sayHi()
test2.howmany()

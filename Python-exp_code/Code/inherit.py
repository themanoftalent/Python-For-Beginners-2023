#! /usr/bin/python
# filename: inherit.py
# Description: inherit of python class

# Note point:
# 1. constructor must be called manually and with self parameter(That's to say has to be compelete and match parameter numbers)
# 2. other functions which call base class must add self paramters must be added too

class base:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def printInfo(self):
        print "%s's gender is %s" % (self.name, self.gender)

class class1(base):
    def __init__(self, name, gender,number):
        base.__init__(self,name, gender) # Note 1
        self.number = number
    def printInfo(self):
        base.printInfo(self)
        print "number is ", self.number

class class2(class1):
    def __init__(self, name, gender, number, addr):
        class1.__init__(self, name, gender, number)
        self.addr = addr
    def printInfo(self):
        class1.printInfo(self) # Note 2
        print "addr is ", self.addr

test1 = base("Ryan", "male")
test1.printInfo()

test2 = class1("Lucy", "female", "0001")
test2.printInfo()

test3 = class2("Lily", "female", "0002", "Wall Street #1008")
test3.printInfo()

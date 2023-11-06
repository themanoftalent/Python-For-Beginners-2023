#! /usr/bin/python
# Filename: object_init
# Description: the constructor in python

class Persion:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print(self.name)

test = Persion("Hello,world")
test.sayHi()

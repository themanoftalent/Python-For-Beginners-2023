#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#


class Persion:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print(self.name)

test = Persion("Hello,world")
test.sayHi()

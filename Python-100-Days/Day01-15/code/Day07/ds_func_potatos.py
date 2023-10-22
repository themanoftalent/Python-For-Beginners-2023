#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

def potatoCost(price, amount, Ptype):
    cost=price*amount
    print(Ptype)
    print(cost)
    print(amount)
    return cost, Ptype, price

potatoCost(10,5,3.4)
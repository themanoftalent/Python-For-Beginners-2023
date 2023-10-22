#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

class BankAccount:

    # constructor or initializer
    def __init__(self, name, money):
        self.__name = name
        self.__balance = money  # __balance is private now, so it is only accessible inside the class

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return "Yetersiz bakiye"

    def checkbalance(self):
        return self.__balance


b1 = BankAccount ('mahmut', 400)
print ('Cekilecek para ',b1.withdraw (500))
b1.deposit (500)

print ('Miktar ',b1.checkbalance ())
print ('Cekilen para ',b1.withdraw (800))
print ('Miktar ',b1.checkbalance ())
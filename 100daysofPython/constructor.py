

#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#
#

class Kullanici:
    name = ''

    # maas = ''

    def __init__(self, name):
        self.name = name
        print (name, end=',')

    def goOutMan(self, hayden, salary, age):
        self.hayden = hayden
        self.maas = salary
        self.age = age
        print ('hayden namaza', hayden, 'maasin', salary, ',', 'age is', age, '.')

    def eatOut(self, hayden, salary, age):
        self.hayden = hayden
        self.maas = salary
        self.age = age
        print ('ahmet', hayden, 'maas', salary, ',', 'yasin ', age, '.')


kullanici1 = Kullanici ('malik')
kullanici1.goOutMan ('kos', 1500, 76)
kullanici1.eatOut ('aptal', 2, 3)

kullanici2 = Kullanici ('Ahmet')
kullanici2.goOutMan ('run', 1000, 38)
kullanici2.eatOut ('saf', 2, 3)

kullanici3 = Kullanici ('Cem')
kullanici1.goOutMan ('kos', 1500, 76)
kullanici3.eatOut ('Ne guzel', 33, 4)

kullanici4 = Kullanici ('Hulya')
kullanici4.goOutMan ('run', 1000, 38)
kullanici4.eatOut ('Oha', 76, 44)

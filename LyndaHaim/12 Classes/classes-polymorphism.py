#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print("The duck cannot bark!")
    def fur(self):
        print("The duck has feathers")


class Dog:
    def bark(self):
        print('woof')

    def fur(self):
        print('The dog has brown and white fur')

    def walk(self):
        print("Walks like a dog")
    def quack(self):
        print("The dog cannot quack!")

def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

    fido = Dog()
    fido.bark()
    fido.fur()

    for a in (donald, fido):
        a.bark()
        a.walk()
        a.fur()
        a.quack()

    in_the_forest(donald)
    in_the_pond(fido)
if __name__ == "__main__": main()

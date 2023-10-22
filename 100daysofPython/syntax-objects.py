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

class Eggs:

    def __init__(self, kind='Frying'):
        self.kind = kind

    def whatSort(self):
        return self.kind


def main():
    frying = Eggs()
    scrambled = Eggs("Scrambled")
    lessFrying = Eggs("Not fried")

    print(frying.whatSort())
    print(scrambled.whatSort())
    print(lessFrying.whatSort())


if __name__ == '__main__':
    main()

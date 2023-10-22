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

def main():
    print('this is the switch.py file')

    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third',
        four = 'fourth',
        five = 'fifth'
    )

    v = 'one'
    print(choices[v])
    a_key = choices.get('ten', 'other')
    print(a_key)



if __name__ == "__main__": main()

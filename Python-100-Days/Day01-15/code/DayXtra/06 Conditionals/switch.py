#!/usr/bin/python3
# switch.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

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

#! /usr/bin/python
# Filename: tuple.py
# Description: a simple for tuple

zoo = ('wolf', 'elephant', 'penguin')
print 'Number of ainals is', len(zoo)

new_zoo = ('monkey', 'snake', 'rabbit', zoo)
print 'Number of new_zoo is', len(new_zoo)
i = 0
while i < len(new_zoo):
    print new_zoo[i],
    i = i + 1 
print '\nEnding output'

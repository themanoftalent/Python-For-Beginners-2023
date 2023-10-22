#! /usr/bin/python

#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

# Filename: using_sys.py
# Description: using sys modules.

import sys

print 'The commander arguments are:'
print 'The script path is', sys.argv[0]
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'

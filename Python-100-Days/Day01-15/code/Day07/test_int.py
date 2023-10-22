#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import sys

def show_sizeof(x, level=0):

	print "\t" * level, x.__class__, sys.getsizeof(x), x

	if hasattr(x, '__iter__'):
		if hasattr(x, 'items'):
			for xx in x.items():
				show_sizeof(xx, level+1)
		else:
			for xx in x:
				show_sizeof(xx, level+1)

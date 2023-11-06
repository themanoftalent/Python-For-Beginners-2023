#!/usr/bin/env python

dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print dict

print dict['a']
dict['a'] = 6

if 'g' in dict:
	print "it is in dict"


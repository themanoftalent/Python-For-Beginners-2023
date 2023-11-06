import re
import _osx_support
import os
import sys
import array
import readline

yazi= ' Regular (we mean) expressions are a powerful :language ' \
      'for matching text patterns. This page gives a basic ' \
      'introduction to regular expressions themselves sufficient ' \
      'for our Python exercises and shows how regular expressions work in Python.' \
      ' The Python "re" module provides regular expression support. '


match = re.search (r':\w\w\w\w\w\w\w\w', yazi)  # w sayisi artikca kelime daha fazla ortaya cikmaktadir.

# burada word ya da kelime veya baska bir sey kullanilabilir sorun degil. mesele iki nokta da:
# If-statement after search() tests if it succeeded

if match:
    print ('found', match.group ())  ## 'found word:cat')

else:
    print ('did not find')

sonuc=yazi.find('s')
print(sonuc)
print('In total it has %s characters.'%len(yazi))

if (yazi.find('ex')!=1):
    print('It is found:','ex')
else:
    print('not found')

if  yazi.endswith('rt')!=1:
    print('Yes it ends with ', '"rt"')
else:
    print('No rt')

print (10 + 5 + (10 * 5) // 2 + 8)
print (type (10))
print (100 % 20)

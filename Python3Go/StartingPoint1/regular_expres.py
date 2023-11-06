'''
Python Regular Expressions

In Python a regular expression search is typically written as:

  match = re.search(pat, str)

The re.search() method takes a regular expression pattern and a string and searches for that pattern within the string.
If the search is successful, search() returns a match object or None otherwise. Therefore, the search is usually
immediately followed by an if-statement to test if the search succeeded, as shown in the following example which
searches for the pattern 'word:' followed by a 3 letter word (details below):

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
  if match:
    print 'found', match.group() ## 'found word:cat'
  else:
    print 'did not find'

The power of regular expressions is that they can specify patterns, not just fixed characters. Here are the most
 basic patterns which match single chars:

    a, X, 9, < -- ordinary characters just match themselves exactly. The meta-characters which do not match themselves
    because they have special meanings are: . ^ $ * + ? { [ ] \ | ( ) (details below)
    . (a period) -- matches any single character except newline '\n'
    \w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. Note that although
    "word" is the mnemonic for this, it only matches a single word char, not a whole word. \W (upper case W) matches
    any non-word character.
    \b -- boundary between word and non-word
    \s -- (lowercase s) matches a single whitespace character -- space, newline, return, tab,
    form [ \n\r\t\f]. \S (upper case S) matches any non-whitespace character.
    \t, \n, \r -- tab, newline, return
    \d -- decimal digit [0-9] (some older regex utilities do not support but \d, but they all support \w and \s)
    ^ = start, $ = end -- match the start or end of the string
    \ -- inhibit the "specialness" of a character. So, for example, use \. to match a period or \\ to match a slash.
    If you are unsure if a character has special meaning, such as '@', you can put a slash in front of it, \@, to
    make sure it is treated just as a character. '''

import re

str = 'an example word:catle!!'
match = re.search (r'word:\w\w\w\w\w', str)  # w sayisi artikca kelime daha fazla ortaya cikmaktadir.
# If-statement after search() tests if it succeeded

if match:
    print ('found', match.group ())  ## 'found word:cat')

else:
    print ('did not find')





print ('\nWriiting in a document \n', '==' * 12)
stbr = open ('newdoc.text', 'w')
stbr.write ('I am wriitng in a doc, What is gonna be inside')
stbr.close ()

restbr = open ('newdoc.text', 'r')
contem = restbr.read ()
print (contem)
restbr.close ()


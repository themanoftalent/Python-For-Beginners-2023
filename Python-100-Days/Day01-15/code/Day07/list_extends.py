#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

# language list
language = ['French', 'English', 'German','Turkish','Russian']

# another list of language
language1 = ['Chinese','Spanish', 'Portuguese','Japanese']

language.extend(language1)

# Extended List
print('Language List: ', language)
language.sort()
print('Sorted lang list',language)
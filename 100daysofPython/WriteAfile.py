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
#

occupations = ['Teachers', 'Doctors', 'Engineers', 'Nurses', 'Presidensts']

with open('occupations.txt', 'w') as newJob:
    for lines in occupations:
        newJob.write(lines)
        newJob.write('\n')  # when we dont add this it is combined

with open('occupations.txt', 'a') as newJob:
    print(23 * '=', file=newJob)
    print('We add file = to write each line separate', file=newJob)

with open('occupations.txt', 'rb') as reader:
    for lines in reader:
        print(lines)

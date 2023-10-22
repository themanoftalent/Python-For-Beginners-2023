#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#
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

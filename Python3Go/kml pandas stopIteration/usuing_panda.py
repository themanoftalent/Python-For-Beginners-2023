import glob2 as glob2
import pandas
import os
import pathlib

fd = pandas.read_csv('word.txt')
print(fd)

print('==========================')
filelist = glob2.glob('*.txt')
print(filelist)
print('==========================')

for file in filelist:
    df = pandas.read_csv(file)
    m = df.mean()
    print(m)
print('==========================')

for file in filelist:
    df = pandas.read_csv(file)
    m = df.mean()
    m = float(m)
    print(m)


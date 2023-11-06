#! /usr/bin/python
# Filename: seq.py
# Description: the use of sequence

shoplist = ['apple', 'banana', 'water']

## Indexing 
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item -1 is', shoplist[-1]

## Slicing 
print 'Item 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is', shoplist[2:]
print 'Item start to 2', shoplist[:2]

## Slicing on string
name = 'deercoder'
print 'character 1 to 3', name[1:3]
print 'character start to -1 end is', name[:-1]


#!/usr/bin/python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('This is the containers.py file.')
    fin = open('utf8.txt', 'r', encoding = 'utf_8')
    fout = open('utf8.html', 'w')

    outbytes = bytearray()
    for line in fin:
        for c in line:
            if ord(c) > 127:
                outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = 'utf_8')
            else:
                outbytes.append(ord(c))
    outstr = str(outbytes, encoding= 'utf_8')
    print(outstr, file = fout)
    print(outstr)
    print("Done!")


if __name__ == "__main__": main()

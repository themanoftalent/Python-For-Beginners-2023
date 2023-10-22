#!/usr/bin/python3
# ops.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the ops.py file.")

    list = []
    list = [1,2,3,4,5,6,7,8,9,10]
    print("list = {}".format(list))
    print("list[0] = {}".format(list[0]))
    print("list[1] = {}".format(list[1]))
    print("list[9] = {}".format(list[9]))

    print("list[0:5] = {}".format(list[0:5]))

    #list = range(0,100)
    #print(list)
    list[:] = range(0,100)
    print(list)

    # 3 possible arguments for slice
    # 1 argument version
    print("list[27] = {}".format(list[27]))
    print("list[27:42] = {}".format(list[27:42]))
    # Stepping across does not include '42' since slice is non-inclusive)
    print("list[27:42:3] = {}".format(list[27:42:3]))
    print("list[27:42:3] = [99,99,99,99,99]")
    list[27:42:3] = [99,99,99,99,99]
    print("list = {}".format(list))


if __name__ == "__main__": main()

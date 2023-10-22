
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#
#

def main():
    stu = {'name': 'Kemal', 'age': 35, 'gender': 'Male'}
    print(stu)
    print(stu.keys())
    print(stu.values())
    print(stu.items())
    print('\n')

    for elem in stu.items():
        print(elem)
        print(elem[0], elem[1])
    if 'age' in stu:
        stu['age'] = 25
        print('New age is ',stu['age'])
    print('\n')

    print(stu)
    stu.setdefault('score', 50)
    print(stu)
    stu.setdefault('score', 100)
    print(stu)
    stu['score'] = 100
    print(stu)


if __name__ == '__main__':
    main()

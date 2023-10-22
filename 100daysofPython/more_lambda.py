#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.


puanlar = [{'x':3,'y':2},
          {'x':4,'y':1}]

puanlar.sort(key=lambda i:i['y'])
print(puanlar)

print(type(puanlar))



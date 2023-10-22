#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

# from pure python list data
from PIL import Image


img = Image.new("L", (104, 104))  # single band
newdata = list(range(0, 256, 4)) * 104
img.putdata(newdata)
img.show()
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
from PIL import Image

img = Image.open('./res/guido.jpg')
print(img.size)
print(img.format)
print(img.format_description)
img.save('./res/guido.png')

img2 = Image.open('./res/guido.png')
img3 = img2.crop((335, 435, 430, 615))
for x in range(4):
    for y in range(5):
        img2.paste(img3, (95 * y , 180 * x))
img2.resize((img.size[0] // 2, img.size[1] // 2))
img2.rotate(90)
img2.save('./res/guido2.png')

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



class Bol:
    texting=''


    def __init__(self,texting):
        textpieces=texting.split(' ')

        self.text_split=textpieces[0]
        self.text_split2=textpieces[1]
        self.text_split3=textpieces[2]
        self.text_split4=textpieces[3]
        self.text_split5=textpieces[-1]


text='Mehmet ahmet cankaya otuzbes zengin'
bolme=Bol(text)
# bolme=Bol('Mehmet ahmet cankaya otuzbes zengin')

print(bolme.text_split)
print(bolme.text_split2)
print(bolme.text_split3)
print(bolme.text_split4)
print(bolme.text_split5)


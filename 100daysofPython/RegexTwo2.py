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
#
#

# .   Match any character
# ^   Match line begin
# $   Match line end
# *   Match previous RE 0 or more times greedily
# *?  Match previous RE 0 or more times non-greedily
# +   Match previous RE 1 or more times greedily
# +?  Match previous RE 1 or more times non-greedily
# ?   Match previous RE 0 or 1 time greedily
# ??  Match previous RE 0 or 1 time non-greedily
# A|B Match either RE A or B
# {m} Match previous RE exactly m times
# {m,n}   Match previous RE m to n times greedily
# {m, n}? Match previous RE m to n times, no-greedily

# ============================================
# [abc]   Match either a, b or c
# [^abc]  Match any character not in this set (i.e., not a, b and c)
# [a-z]   Match the range from a to z
# [a-f2-8]    Match the range from a to z or the range from 2 to 8
# [a\-z]  Match a, - or z
# [a-]    Match a, -
# [-a]    Match -, a
# [-a]    Match -, a
# [{}*|()[]+\^$.?]    Match either one of the chacters in []{}*|()+^$?.
# ============================================


import re

# match=re.search('What', 'string is not What we look')
# print(match.group())

# def Find_some(pat,text):
#     match=re.search(pat, text)
#     if match.group():
#         print('Found pattern as :',match.group())
#     else:
#         print('Not found')


# Find_some('nolur', 'nolur gel buaraya')


# def Found(pat,text):
#     esles=re.search(pat, text)
#     if esles.group():
#         print('Found :', esles.group())
#     else:
#         print('error')


# Found('gel', 'gel bana gel abana abana ')


# import re

# regex = r"paragraf sonu"

# test_str = "Sayfa ya da paragraf sonu dışındaki herhangi bir karakteri temsil eder.\
#  Örnek olarak “k.re” ifadesi “küre”, “kare”, “kore”, “kere” ile eşlenecektir."

# matches = re.finditer(regex, test_str, re.MULTILINE)

# for matchNum, match in enumerate(matches, start=1):

#     print ("Match {matchNum} was found at {start}-{end}: {match}".\
#         format(matchNum = matchNum, start = match.start(), \
#             end = match.end(), match = match.group()))

#     for groupNum in range(0, len(match.groups())):
#         groupNum = groupNum + 1

#         print ("Group {groupNum} found at {start}-{end}: {group}".\
#             format(groupNum = groupNum, start = match.start(groupNum), \
#                 end = match.end(groupNum), group = match.group(groupNum)))

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

# import re

# regex = r"akif"

# test_str = "Hesaplanmış Metrikler (calculated metrics) gtag.js ve analytics.js \
# kurulumlarına sahip -klasik analytics (ga.js) desteği bulunmamaktadır- web siteleri \
# için geçerli olan bir 1235.567 Universal Analytics özelliğidir ve kullanıcıların Google Analytics \
# metriklerini kullanarak yeni 1235.567 metrikler oluşturabilmelerini ve raporlarda kullanabilmelerini \
# mümkün kılar. Bu sayede kullanıcı tanıakifmlı metrikleri kullanarak daha alakalı analizler yapabiliriz, \
# raporların kapsamını genişletebiliriz. Hesaplanmış Metrikler Google Analytics kullanıcılara güncel \
# durumda (Mart 2019)  1235.567 Beta olarak sunulmaktadır."

# matches = re.finditer(regex, test_str, re.MULTILINE)

# for matchNum, match in enumerate(matches, start=1):

#     print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, \
#         start = match.start(), end = match.end(), match = match.group()))

#     for groupNum in range(0, len(match.groups())):
#         groupNum = groupNum + 1

#         print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, \
#             start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# import re

# metin = "No gain no pain"

# kontrol=re.match('No', metin)
# print(kontrol)
# print(kontrol.span())
# print(kontrol.group())


import re

# metin = "No gain no pain However, no gain soreness, no gain\
#  just doesn't have the same ring to it as \
#  no pain, no gain Listen your body gain. It will tell you. ... \
#  Pain associated with injury is something you don't want to encounter, \
#  but some discomfort or soreness from challenging your muscles is normal and expected. "

# kontrol=re.search('gain', metin)
# print(kontrol)
# print(kontrol.span())
# print(kontrol.group())

# regex only for text files

# liste1 = ['physics', 'chemistry', 1997, 2000]

# for eleman in liste1:
#     if re.search('physics', eleman):
#         print('Found',eleman,'\n')


# metin2='ilim ilim ilmektir'
# print(re.findall('ilim',metin2))

# nexit=re.search('ilim',metin2,re.MULTILINE)
# print(nexit.group())


# metin3='Ahmet araba icin 34000$ odemis '

# print(re.findall('[0-9]+\$',metin3))

# * olsun olmasin


liste4 = ['abef', 'abcdef', 'abcfg', 'abhgs']

for eleman4 in liste4:
    if re.search('ab(cd)*ef', eleman4):
        print(eleman4)


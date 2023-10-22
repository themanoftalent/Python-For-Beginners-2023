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

import os
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

directoryh=('/Users/darwin/Desktop/IJERT-Multiple_Step_of_Image_Processing.pdf')


# creating a pdf file object 
with open(directoryh, 'rb') as f:
    pdfReader = PyPDF2.PdfFileReader(f) 
    print(pdfReader.numPages) 
    pageObj = pdfReader.getPage(0) 
    print(pageObj.extractText()) 

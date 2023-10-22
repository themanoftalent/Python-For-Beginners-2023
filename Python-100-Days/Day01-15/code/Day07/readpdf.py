#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

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

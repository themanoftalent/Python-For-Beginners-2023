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
import pathlib
import simplekml

kml=simplekml.Kml()
kml.newpoint(name='samsan',coords=[(15,15)])
print(kml)

kml.save(os.path.expanduser("~/Desktop/bura/Points2.kml"))



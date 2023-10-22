#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import os
import pathlib
import simplekml

kml=simplekml.Kml()
kml.newpoint(name='samsan',coords=[(15,15)])
print(kml)

kml.save(os.path.expanduser("~/Desktop/bura/Points2.kml"))



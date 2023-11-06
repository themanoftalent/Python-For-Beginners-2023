import os
import pathlib
import simplekml

kml=simplekml.Kml()
kml.newpoint(name='samsan',coords=[(15,15)])
print(kml)

kml.save(os.path.expanduser("~/Desktop/bura/Points2.kml"))



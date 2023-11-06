import os
import pathlib
import simplekml


longitude = input("Enter longitude: ")
latitude = input("Enter longitude: ")

kml = simplekml.Kml()
kml.newpoint(name="Sample", coords=[(longitude, latitude)])
kml.save(os.path.expanduser("~/Desktop/bura/Points.kml"))

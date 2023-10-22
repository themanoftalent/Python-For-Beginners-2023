import os

# Your path here e.g. "C:\Program Files\text.txt"
# For access purposes: "C:\\Program Files\\text.txt"
if os.path.exists("~/Desktop/bura/points.kml"):
    print ("File found!")
else:
    print ("File not found!")

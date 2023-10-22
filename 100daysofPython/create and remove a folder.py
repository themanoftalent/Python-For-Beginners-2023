import os
import pathlib
import pathlib
#to create a folder
newpath = os.path.expanduser('~/Desktop/bura/folderz')
if not os.path.exists(newpath):
    os.makedirs(newpath)

#to remove a folder
newpath = os.path.expanduser('~/Desktop/bura/myfold')
if os.path.exists(newpath):
    os.removedirs(newpath)

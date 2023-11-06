#! /usr/bin/python
# Filename: auto-backup-v2.py
# Description: This script is used to auto backup files.
import time
import os
## The source files which needs backup
source = ['/home/ryan/bin', '/home/ryan/myDoc']

## The destination directory to store the zip files
destination = '/home/ryan/'


## The zip file name
date = time.strftime("%Y%m%d")
dir_name = destination + date
filename = time.strftime("%H%M%S")+ '.zip'
print 'filename is',filename

## judge wheter the dir is exist
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print 'Successfully create directory'

### command to excute
command = "zip -qr %s %s"%(dir_name + os.sep + filename, ' '.join(source))
print 'comand is',command

## excute the command
if os.system(command) == 0:
    print 'Backup successfully!'
else:
    print 'Failure'

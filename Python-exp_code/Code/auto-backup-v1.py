#! /usr/bin/python
# Filename: auto-backup.py
# Description: This script is used to auto backup files.
import time
import os
## The source files which needs backup
source = ['/home/ryan/bin', '/home/ryan/myDoc']

## The destination directory to store the zip files
destination = '/home/ryan/'


## The zip file name
filename = time.strftime("%Y%m%d%H%M%S") + '.zip'
print 'filename is',filename

### command to excute
command = "zip -qr %s %s"%(destination + filename, ' '.join(source))
print 'comand is',command

## excute the command
if os.system(command) == 0:
    print 'Backup successfully!'
else:
    print 'Failure'


#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import os
import shutil

# Source path
source = "/Users//Downloads/hey/afile.pdf"
# Destination path
destination = "/Users//Downloads/say"

# Copy the content of
# source to destination
file_last_dest = shutil.copy(source, destination)

print("After copying file:")
print(os.listdir(destination))

print('........................')
# Print path of newly
# created file
print("Printing the Destination path:", file_last_dest)


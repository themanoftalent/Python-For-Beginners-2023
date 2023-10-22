#!/usr/bin/env python

#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import re
match = re.match('Hello[ \t].(.*)world', 'Hello    Python world')
print match.group(1)

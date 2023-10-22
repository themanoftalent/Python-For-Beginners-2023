#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

# How to Use %-formatting
# String objects have a built-in operation using the % operator, which you can use to format strings.
# Here’s what that looks like in practice:


name = "Cemil"
last_name = 'Kaya'
age = 35
profession = 'comp eng'
affiliation = 'a university'
print("Hello, %s." % name)

print("==================================")

# 2: str.format()
# This newer way of getting the job done was introduced in Python.
# How To Use str.format()
# str.format()  is an improvement on %-formatting.
# It uses normal function call syntax and is extensible through the __format__() method on
# the object being converted to a string.
# With str.format(), the replacement fields are marked by curly braces:

print("Hello, {}. You are {}.".format(name, age))

print("==================================")

print(("Hello, {first_name} {last_name}. You are {age}. " +
       'You are a {profession}. You were a member of {affiliation}.') \
      .format(first_name=name, last_name=last_name, age=age, \
              profession=profession, affiliation=affiliation))

print("==================================")

print(("Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You are a member of {affiliation}.") \
      .format(first_name=name, last_name=last_name, age=age, profession=profession, affiliation=affiliation))

print("==================================")

# Multiline f-Strings
# You can have multiline strings:

name = "Esra"
profession = "Nurse"
affiliation = "Medical"
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"you are {affiliation}")

print(message)

print("==================================")

# import timeit
#
# print(timeit.timeit("""name = "Eric"
# age = 39
# '%s is %s.' % (name, age)""", number=10000))


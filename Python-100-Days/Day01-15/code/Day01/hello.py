#!/usr/bin/python
# dev:akifcifci

print('hello, world!')
# print("we can add space by using \n or etc.")

print('hello', 'world', sep=', ', end='!')
print('Goodbye, world', end='!\n')

hello = 'Hello man'
print(hello)

print("{}".format(hello))

print('=================================')

#=================================
first_name = "Akif"
age = 30
last_name = "CIFTCI"
profession = "Teacher"
affiliation = "IA"
#=================================

print(f"Hello, {first_name}. You are {age}.")  # this Is f string we can use format instead of that.
print('=================================')

print("Hello, {}. You are {}.".format(first_name, age))
#print('or')
print("Hello, {1}. You are {0}.".format(age, first_name))
#print('and\n')

print('=================================')
print(("Hello, {first_name} {last_name}. You are {age}. "
       "You are a {profession}. You are a member of {affiliation}.")
      .format(first_name=first_name, last_name=last_name, age=age,
              profession=profession, affiliation=affiliation))

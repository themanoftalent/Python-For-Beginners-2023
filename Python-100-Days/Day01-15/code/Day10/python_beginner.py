#editor and coder=mynonofficial


"""number"""
power = 5 ** 2  # ** is the power operator, higher precedence than +/-
integer_division = 5 // 2  # // is the integer division operator; / will always return a float
complex_number = 3 + 6j  # Python has built in support for complex number, denoted by j or J
complex_number_a, complex_number_b = 2 + 4j, 7 + 8j  # multiple assignment
# in Python console, we can use the variable _ to indicate the last printed expression
# one should use _ as read only and never assign value to _ as it creates another local variable called _
# we can use float() to convert a string to numbers

"""string"""
string_quotes = 'String are represented inside single quotes, ' + "or double quotes. "
string_jump = 'It\'s okay to use \ to jump a single quotes. ' + "But let's use double quotes instead. "
print('I have a complex number read', complex_number)  # print connected by , will automatically lead to a space
raw_string = r'It\'ll be printed.'  # r'' makes a raw string that everything will be printed regardless of \
print("""\
Choose: Type    [OPTIONS]
         -g      group
         -r      ring
         -f      field\
        """)  # use triple quotes to create multiple line strings; the \ in first line prevent printing a new line
string_operator = 'nico' * 2 + 'ni' '~'  # * repeats string and two adjacent string add to each other
print(string_operator)
'''
strings are indexed: string_operator[0] = 'n', string_operator[-1] = '~' with negative index counting from right
string_operator[1:5] = 'icon' obtaining substring with character from 1 (included) to 5 (excluded) called slicing
string_operator[:5] + string_operator[5:] = 'niconiconi~'
indices are pointing between characters: 0 n 1 i 2 c 3 o 4 n 5 i 6 c 7 o 8 n 9 i 10 ~ 11
negative indices are 10 = -1, 9 = -2, etc.; slicing is obtaining the characters between the two indices
out-of-range slice indices are handled gracefully string_operator[10:50] = 'i~'
'''
# strings are immutable: assigning to an indexed position in the string results in an error
string_length = len(string_operator)

"""list"""
int_list = [1, 4, 9]  # indexed as strings
squares = int_list + [16, 25]
# lists are mutable - feel free assigning values to their entries
squares.append(36)  # add new item 36 to the end of the list
# we can change entries or clear strings by slicing
squares[1:3] = []  # changes squares to [1, 16, 25, 36]
squares[:] = []  # clear squares to []
list_length = len(squares)
int_nested = [int_list, int_list]  # creates a nested list [[1, 4, 9], [1, 4, 9]]

"""while"""
a, b = 0, 1
while b < 20:  # while loop executes as long as this is true
    print(b)
    a, b = b, a + b
else:
    print('end of series')  # executed when the while condition is false
# this gives the Fibonacci series

"""if"""
if power < 0:
    power = 0
    print('power of imaginary number')
elif power == 0:
    print('it\'s just zero')
elif power == 1:
    print('additional identity')
else:
    print('not interested')

# a blank line is required to indicate the completion of a block

"""for"""
# for loop works like an operator with a list as its domain
# x is a dummy variable representing a member of int_list; for loop execute in the index order of int_list
for x in int_list:
    if x > 2:
        print(x)
else:
    print('for-list exhausted')

# else of a for loop will execute until the exhaustion of the list

"""range()"""
inc = 0
for i in range(5):  # range(5) works as [0, 1, 2, 3, 4]
    inc += i

list_range = []
for i in range(5, 10):  # range(5,10) works as [5, 6, 7, 8, 9]
    list_range.append(i)

for i in range(10, 20, 3):  # range(min, max, step) works as [10, 13, 16, 19]
    list_range.append(i)

# to iterate over indices of a list/string, combine range() and len()
for i in range(len(int_list)):
    print(i + 1, int_list[i])

"""
note that, the result of print(range(5)) is range(0, 10) and obviously not a list
range() doesn't create a list but an object returning the successive items of a sequence when we iterate over it
we say range() is iterable and the for statement is an iterator
the function list() is also iterable and creates lists from iterable objects
"""
print(list(range(1, 30, 7)))

"""break"""
# breaks out of the smallest enclosing for or while loop
# inside a for/while-else structure, the else body won't be executed if the loop is terminated by break

"""continue"""
# continue the next iteration of the loop

"""pass"""
# pass statement is a void statement who does nothing, similar to a single ; in C++

"""function"""


def fib(n):  # def function(formal_parameter1, formal_parameter2, ...)
    """We want to print a Fibonacci series up to n."""
    # the previous line is the documentation string of the function fib()
    a, b = 0, 1  # defines two local variable stored in the local symbol table of fib()
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()  # this prints an empty line
    # looks like we do not have a return statement but every function returns a value; fib() returns None


fib(2000)  # calling fib() function
print(fib(500))  # executes fib(1000) and returns None

"""
we can only call but cannot assign a global variable within a function (unless named in a global statement)
when calling a variable, say b in fib(), first find it in the local symbol table fib(),
then the local symbol table of any mother function of fib(), then the global symbol table
the actual parameters (arguments), n = 2000 for example, are saved in the local symbol table when it is called
arguments are passed using call by value (value an object reference, not the value of the object)
when a function calls another function, a new local symbol table is created for that call
function name is a type recognized by the interpreter as a user-defined function
"""
f = fib  # we can assign function name like this
f(2000)  # this is exactly fib(2000)


def fib_list(n):
    """Return a list of Fibonacci series up to n."""
    ans = []
    a, b = 0, 1
    while a < n:
        ans.append(a)
        a, b = b, a + b
    return ans


f_list = fib_list(500)  # call the function
print(f_list)

"""
a method is a function belongs to an object and is written obj.method
different types have different methods that can have the same name without causing ambiguity
ans.append(a) calls a method of the list object ans, equivalent to ans = ans + [a]
"""

"""function argument"""
power = 4


def ask_ok(prompt, retry=power, reminder='Please try again!'):  # no space around = when assigning default value
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retry -= retry
        if retry < 0:
            raise ValueError('invalid user response')
        print(reminder)


power = 9
"""
in the function ask_ok, only the argument prompt is mandatory with the other two arguments having default value
however we can call anything if we don't want the default value like ask_ok('OK to delete all?', 5, 'yes/no only!')
the default values are evaluated at the point of function definition in the defining scope, and evaluated only once
so further change of power = 9 is not recognized by the function; the function only knows retry=4
however, if the default value is mutable, the value may change every time when we call the function
this can be prevented; see https://docs.python.org/3/tutorial/controlflow.html#default-argument-values for details
a function can also be called by keyword arguments like ask_ok(prompt='OK or not', retry=2)
however, mixing of keyword and non-keyword arguments is not allowed; we cannot have ask_ok(prompt='OK or not', 2)
"""


def menu(kind, *ent, **sides):  # *ent is a tuple, **sides is a dictionary containing all arguments apart from kind
    print('The kind is', kind + '. ')
    print('-' * 20, ' entree ', '-' * 19)
    for entree in ent:
        print(entree)
    print('-' * 20, ' sides ', '-' * 20)
    keys = sorted(sides.keys())  # we have to sort them first and print otherwise the order is undefined
    for sid in keys:
        print(sid, ":", sides[sid])


menu('Panda Express', 'Honey Walnut Shrimp', 'Shanghai Steak', s1='Veg Roll', s2='Chicken Roll', s3='Crab Rangoon')

# now consider the situation that the argument is already a list with each entries an argument
# we have to unpacking argument list by * operator and a dictionary by ** operator
args = [3, 6]
print(list(range(*args)))  # this is equivalent to print(list(range(3, 6))), * unpacking the list


def meal(kind, entree, side):
    print('This is a meal from', kind, 'with', entree, 'and', side + '. ')


dic_menu = {'kind': 'Panda Express', 'entree': 'shrimp', 'side': 'rangoon'}
meal(**dic_menu)  # ** unpacking the dictionary

"""lambda"""


def increment(n):
    return lambda x: x + n


f = increment(42)
# small handling function can be represented by lambda, by the form lambda x: f(x), with f(x) an expression of x
print(f(0), f(1), f(10), f(100))
# it's also possible to use lambda to return a function passing a small function as an argument

"""documentation string"""
# the first line of the documentation string should always be a short concise summary of the object's purpose
# the first line usually don't contain the object's name or type; it should start with capital letter and end with a .
# if there are more lines, the second line should be blank to separate the summary and the body

"""function annotation"""


# optional metadata about types; stored in __annotation__ attribute of the function as a dictionary
# have no effect on any other part of the function


def demo(ham: str, eggs: str = 'organic_eggs') -> str:  # function(parameter: type_annotation=default_value) -> type
    print('Annotation:', demo.__annotations__)
    print('Argument:', ham, eggs)
    return print(ham + ' and ' + eggs)


demo('spam')

"""coding style"""
# name classes as CamelCase and functions/methods as lower_case_with_underscore
# always use self as the name for the first method argument

print('==================ara==================')
"""Python Tutorial Chapter 5"""

from collections import deque  # Module 01
from math import pi  # Module 02

"""list"""
a, b = [2, 4, 6, 8], [1, 3, 5, 7]

a.append(10)  # add an item at the end of the list
print(a)

a.extend(b)  # appending a whole list at the end of a
print(a)

a.insert(2, 5)  # insert 5 to the position index 2 and move the previous item of position 2 to position 3; return None
print(a)

a.remove(5)  # remove the first item in the list whose value is 5; return None
print(a)

c = a.pop()  # remove the last item if no value assigned to pop() and return the removed value
print(a, c)

a.pop()  # if we do not assign a.pop() to some object, only the last item is removed
print(a)

c = a.pop(5)  # remove the item with index 5 and return the removed value
print(a, c)

a.clear()  # remove all items from the list
print(a)

a = [8, 4, 6, 2]

c = a.index(4)  # return the index of the first item whose value is 6; if not exist, return an error
print(a, c)

a.reverse()  # reverse the list
print(a)

a.sort(key=None, reverse=False)  # sort the items of the list in place; return None
print(a)

c = a.copy()  # return a copy of the list a
print(a, c)

del a[0]  # delete the 0th term of a without returning the value of the 0th term
print(a)

a.extend(c)
print(a)
del a[3:5]  # delete the 3rd and 4th terms
print(a)
del a[:]  # clear a
print(a)

del a  # this will remove the variable completely
# print(a) will raise an error saying name 'a' is not defined

"""
it's convenient to use lists as stacks: the last element added to the list will be the first element retrieved later
to add an item, use a.append(); to remove an item, use a.pop()
the (conventionally speaking) top of the stack is actually at the end of the list
it's also possible to use lists as queues: the first element added to the list will be the first one retrieved later
however, lists are not efficiently handled as queues
because each time retrieving something from the beginning, all the other elements have to be shifted by one
use collections.deque to fast appending and popping from both ends (using Module 01)
"""

prime = deque([0, 1, 2, 3, 5, 7, 11, 13, 17, 19])
prime.append(23)
b = [29, 31, 37]
prime.extend(b)
prime.popleft()  # pop the first item
prime.popleft()
print(prime)

# we can create a list by loops
squares = []
for i in range(1, 10):
    squares.append(i ** 2)
print(squares)

# but there's more concise methods
squares_concise = list(map(lambda x: x ** 2, range(1, 10)))
print(squares_concise)

# or equivalently
squares_more_concise = [x ** 2 for x in range(1, 10)]  # called a list comprehension
print(squares_more_concise)

# list comprehension has the form: [(expression) for/if clause], with each expression parenthesized like (x, y, z, ...)
pairs = [(x, y) for x in [1, 2, 3] for y in [3, 4, 5] if x != y]  # all pairs (x,y) from two sets with different value
print(pairs)

# list comprehensions can contain complex expression (using Module 02)
pi_round = [str(round(pi, i)) for i in range(1, 8)]
print(pi_round)

matrix_row = [  # each sublist is a row of the matrix
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(matrix_row)

matrix_column = [[row[i] for row in matrix_row] for i in range(4)]  # transpose matrix_row into a collection of columns
print(matrix_column)

matrix_column_zip = list(zip(*matrix_row))  # zip() function does the transpose with * unpacking the matrix
print(matrix_column_zip)  # note that [1, 5, 9] is written as a tuple (1, 5, 9) (instead of sublist) with zip()

"""tuple"""
# tuple is an immutable datatype
t = 12345, 67890, 'number', 'integer'  # t is then a tuple
print(t)

t_nested = t, (765, 432, 'another tuple')
print(t_nested)

# t[1] = 6789 raise an error as tuple is immutable
t_mutable_object = ([3, 7, 1], [4, 5, 6])  # but a tuple can contain other mutable objects
print(t_mutable_object)

t_empty = ()
t_singleton = 'hello',  # need a comma
a, b = t_mutable_object  # unpacking a tuple: the number of variables on the LHS must agree with the tuple on RHS

"""sequence"""

"""
list, string and tuple are examples of the sequence data type
sequences can be compared in lexicographical order - the first pair determines the order is the order of the sequences
[1, 2, 3] > [1, 1, 1] because 1 == 1, 2 > 1
(1, 2, 1) < (1, 2, 3) because 1 == 1, 2 == 2, 1 < 3
{1, 2, 4} > {1, 2, 3, 4} because 1 == 1, 2 == 2, 4 > 3
(1, 2) < (1, 2, 0) because 1 == 1, 2 == 2, 0 > ()
(1, 2, 3) == (1.0, 2.0, 3.0) because 1 == 1.0, 2 == 2.0, 3 == 3.0
(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4) because ('aa', 'ab') < ('abc', 'a') as 'aa' < 'abc'
"""

"""set"""
# set is a data type that is unordered with no duplicate elements
set_prime = {2, 3, 5, 7, 3, 11, 13, 17, 17, 19}
T_bool = 11 in set_prime  # returns True
F_bool = 12 in set_prime  # returns False
print(set_prime)  # repeated elements are combined

set_empty = set()  # cannot use set_empty = {} as it creates an empty dictionary

c = set('is_a_good_idea')
print(c)  # it will decompose a string into unique letters
d = set('not-trivial_idea')

diff_cd = c - d  # gives the letters that is in a but not in b
union_cd = c | d  # either in c or d
intersection_cd = c & d  # both in c and d
intersection_complementary_cd = c ^ d  # in c or d but not both
print(intersection_complementary_cd)

c = {x for x in 'not_a_good_idea' if x not in 'god'}

"""dictionary"""
# dictionaries are indexed by keys, which can be any immutable type like strings and numbers
# a dictionary is an unordered key:value pairs; this requires keys to be unique within one dictionary
# if we store value into an existing key, the old value will be forgotten

pokemon = {'Bulbasaur': 1, 'Ivysaur': 2, 'Venusaur': 3, 'Charmander': 4, 'Charmeleon': 5, 'Charizard': 6}
print(pokemon['Ivysaur'])
pokemon_names = list(pokemon.keys())  # all the keys in random order
pokemon_names_sorted = sorted(pokemon.keys())  # in sorted order
pokemon = dict([('Squirtle', 7), ('Wartortle', 8), ('Blastoise', 9)])  # can also be generated by dict()
dict_prime_power = {x: x ** 2 for x in (2, 3, 5, 7, 11)}  # dictionary comprehension
print(dict_prime_power)

# it's possible to retrieve the key and value at the same time using items()
for key, value in pokemon.items():
    print(key, value)

"""looping"""
# use enumerate() to a sequence will get the corresponding index and value
for index, value in enumerate(a):
    print(index, value)

# to loop over two or more sequences at the same time, we use the zip() function
questions = ['name', 'ability', 'occupation']
answers = ['Marisa', 'using magic', 'magician']
for q, a in zip(questions, answers):
    print('What is her {0}?    It is {1}.'.format(q, a))

# to loop over a reversed or sorted sequence, just use reversed() and sorted()
# use in operator to determine if a value is in a sequence: only test the value of the elements of a sequence
print(4 not in [2, 3, 4])
print([1] in [1, 4, 5])
print([1] in [[1], 4, 5])

# comparisons can be nested
print(6 < 7 <= 7 == 7 <= 7 < 8)

# comparisons can be linked by Boolean operators and/or, which are short-circuit operators
# comparisons can be negated by not; not has higher priority than and/or
print(not 3 > 4 and 6 <= 6)


"""Python Tutorial Chapter 6 to Chapter 8"""
print('===============================================================')
import fibo  # Module 01
import builtins  # Module 02
import math  # Module 03

"""module"""

"""
module is a file containing definitions and statements
statements in the module will only execute at the first time the module name is in an import statement
thus statements in a module are intended to initialization
within a module, the module's name, as a string, is available as the value of the global variable __name__
we imported Module 01 at beginning, which calculates the Fibonacci numbers
"""

fibo.fib(1000)
print(fibo.fib2(100))
print(fibo.__name__)
fib = fibo.fib  # it's possible to store a function conveniently from a module
fib(500)

"""
to import a module, alternatively, we can use from fibo import fib, fib2
or from fibo import *, which imports all names except names beginning with _
we can run a module as an independent script: see fibo.py for details
once there is an import statement, Python searches built-in module first, then name.py in the directories of sys.path
sys.path contains: script directory, PYTHONPATH, installation-dependent default; can be modified
to speed up loading, Python caches the complied module in __pycache__ under module.version.pyc
Python doesn't check cache when the module is loaded in the command line or the module doesn't have a source
"""

"""sys"""
# import sys  # Module 02
# sys.ps1, sys.ps2 modifies the two strings of primary and secondary prompt in interaction mode
# sys.path.append() gives one more path for storing module

"""dir()"""
print(dir(fibo))  # gives all the names a module defines
print(dir(builtins))  # to print all built-in modules, import Module 02 first

"""package"""
# package is a collection of modules; dotted name: A.B means a sub-module named B in a package named A
# the 1__init__.py defines a list __all__ that contains module names being imported when calling: from XX import *
# __path__ gives a predefined path before running the module that might be modified

"""string formatting"""
# we can use str() or repr() to convert anything into a string; str() is for human reading and repr() is for computers
# repr() of a string contains quotes and backslashes
print('Azuki\n')
print(str('Azuki\n'))
print(repr('Azuki\n'))

# we can use methods str.rjust() str.ljust() and str.center() to format a string
print('  x   x^2   x^3')
for x in range(1, 11):
    print(repr(x).rjust(3), repr(x * x).rjust(4), end=' ')
    print(repr(x * x * x).rjust(5))

# str.format() can assign values to placeholder {} in a string; numbers in {} indicates locus in str.format()
print('We are the {} who say "{}!"'.format('lions', 'Roar'))
print('We are the {1} who say "{0}!"'.format('Ni', 'knights'))
print('{name} used her spell card {sc}!'.format(name='Marisa', sc='Master Spark'))
# we can convert the text value by !a, !s and !r; each corresponding to ascii(), str(), repr()
spell_marisa = 'Master Spark'
print('Kirisame Marisa used {!a}.'.format(spell_marisa))
# we can use : to call for additional format; Module 03 is used here to show the number pi to 5 digits after decimal
print('PI = {0:.5f}'.format(math.pi))

# put an inter after : will give a minimum number of characters wide, which makes tables pretty
spell = {'Final Spark': 1000, 'Hourai Doll': 800, 'Philosopher\'s Stone': 600}
for name, power in spell.items():
    print('{0:25} ==> {1:10d}'.format(name, power))  # d in the second format means increasing order

"""file"""

"""
open() returns a file object; open(filename, mode)
filename is the string containing the filename
mode: 'r' reading only; 'w' writing only; 'a' appending only; 'r+' both reading and writing;
mode will be 'r' if omitted
files are mostly opened in text mode, with line ending converted to \n; possible to open files in binary mode
fr.read() will return the entire contents of the file
fr.readline() will return a single line; it returns an empty string at the end of file
to read all lines use list(fr) or fr.readlines()
"""

fr = open('frexp', 'r')  # fr is an example file object of a reading only file

fr.readline()  # read the first line silently
fr.readline()  # read the second line silently
print('\n' + fr.readline(), end='')  # read the third line and print
#  we can even loop through the file objects
for line in fr:
    print(line, end='\n')

fw = open('fwexp', 'w')  # fw is an example file object of a writing only file

"""
fw.write(string) writes the contents of a string to the file, returning the number of characters written
objects other than string must be converted by str() before writing
fw.tell() gives the number of bytes from beginning if in binary mode
use fw.seek(offset, from_what) to go to a specific position;
offset is regarding to a reference point with 0 the reference position and +/- a number to another position
from_what=0 means reference at beginning; =1 reference means at current position; =2 means at the end of the file
in text mode, only seek from beginning is allowed except seek(0,2); only valid offset values are returned from f.tell()
"""

fw.write('It\'s the first line of a test. \n')
print(fw.tell())  # since we are in text mode instead of binary mode, fw.tell() tells nothing

# always close the files after using them
fr.close()
fw.close()

# it's convenient to use the with keyword when handling with files as it automatically close the file after handling
with open('frexp', 'r') as f:
    read_data = f.read()

print(read_data)

# JSON = JavaScript Object Notation can be used to serializing/de-serializing a a file/data

"""exception"""
# error detected during execution; example: 1/0, undefined identifier, '2'+2

print('===============================================================')

"""Python Tutorial Chapter 6 to Chapter 8"""

import fibo  # Module 01
import builtins  # Module 02
import math  # Module 03

"""module"""

"""
module is a file containing definitions and statements
statements in the module will only execute at the first time the module name is in an import statement
thus statements in a module are intended to initialization
within a module, the module's name, as a string, is available as the value of the global variable __name__
we imported Module 01 at beginning, which calculates the Fibonacci numbers
"""

fibo.fib(1000)
print(fibo.fib2(100))
print(fibo.__name__)
fib = fibo.fib  # it's possible to store a function conveniently from a module
fib(500)

"""
to import a module, alternatively, we can use from fibo import fib, fib2
or from fibo import *, which imports all names except names beginning with _
we can run a module as an independent script: see fibo.py for details
once there is an import statement, Python searches built-in module first, then name.py in the directories of sys.path
sys.path contains: script directory, PYTHONPATH, installation-dependent default; can be modified
to speed up loading, Python caches the complied module in __pycache__ under module.version.pyc
Python doesn't check cache when the module is loaded in the command line or the module doesn't have a source
"""

"""sys"""
# import sys  # Module 02
# sys.ps1, sys.ps2 modifies the two strings of primary and secondary prompt in interaction mode
# sys.path.append() gives one more path for storing module

"""dir()"""
print(dir(fibo))  # gives all the names a module defines
print(dir(builtins))  # to print all built-in modules, import Module 02 first

"""package"""
# package is a collection of modules; dotted name: A.B means a sub-module named B in a package named A
# the 1__init__.py defines a list __all__ that contains module names being imported when calling: from XX import *
# __path__ gives a predefined path before running the module that might be modified

"""string formatting"""
# we can use str() or repr() to convert anything into a string; str() is for human reading and repr() is for computers
# repr() of a string contains quotes and backslashes
print('Azuki\n')
print(str('Azuki\n'))
print(repr('Azuki\n'))

# we can use methods str.rjust() str.ljust() and str.center() to format a string
print('  x   x^2   x^3')
for x in range(1, 11):
    print(repr(x).rjust(3), repr(x * x).rjust(4), end=' ')
    print(repr(x * x * x).rjust(5))

# str.format() can assign values to placeholder {} in a string; numbers in {} indicates locus in str.format()
print('We are the {} who say "{}!"'.format('lions', 'Roar'))
print('We are the {1} who say "{0}!"'.format('Ni', 'knights'))
print('{name} used her spell card {sc}!'.format(name='Marisa', sc='Master Spark'))
# we can convert the text value by !a, !s and !r; each corresponding to ascii(), str(), repr()
spell_marisa = 'Master Spark'
print('Kirisame Marisa used {!a}.'.format(spell_marisa))
# we can use : to call for additional format; Module 03 is used here to show the number pi to 5 digits after decimal
print('PI = {0:.5f}'.format(math.pi))

# put an inter after : will give a minimum number of characters wide, which makes tables pretty
spell = {'Final Spark': 1000, 'Hourai Doll': 800, 'Philosopher\'s Stone': 600}
for name, power in spell.items():
    print('{0:25} ==> {1:10d}'.format(name, power))  # d in the second format means increasing order

"""file"""

"""
open() returns a file object; open(filename, mode)
filename is the string containing the filename
mode: 'r' reading only; 'w' writing only; 'a' appending only; 'r+' both reading and writing;
mode will be 'r' if omitted
files are mostly opened in text mode, with line ending converted to \n; possible to open files in binary mode
fr.read() will return the entire contents of the file
fr.readline() will return a single line; it returns an empty string at the end of file
to read all lines use list(fr) or fr.readlines()
"""

fr = open('frexp', 'r')  # fr is an example file object of a reading only file

fr.readline()  # read the first line silently
fr.readline()  # read the second line silently
print('\n' + fr.readline(), end='')  # read the third line and print
#  we can even loop through the file objects
for line in fr:
    print(line, end='\n')

fw = open('fwexp', 'w')  # fw is an example file object of a writing only file

"""
fw.write(string) writes the contents of a string to the file, returning the number of characters written
objects other than string must be converted by str() before writing
fw.tell() gives the number of bytes from beginning if in binary mode
use fw.seek(offset, from_what) to go to a specific position;
offset is regarding to a reference point with 0 the reference position and +/- a number to another position
from_what=0 means reference at beginning; =1 reference means at current position; =2 means at the end of the file
in text mode, only seek from beginning is allowed except seek(0,2); only valid offset values are returned from f.tell()
"""

fw.write('It\'s the first line of a test. \n')
print(fw.tell())  # since we are in text mode instead of binary mode, fw.tell() tells nothing

# always close the files after using them
fr.close()
fw.close()

# it's convenient to use the with keyword when handling with files as it automatically close the file after handling
with open('frexp', 'r') as f:
    read_data = f.read()

print(read_data)

# JSON = JavaScript Object Notation can be used to serializing/de-serializing a a file/data

"""exception"""
# error detected during execution; example: 1/0, undefined identifier, '2'+2

print('=================================================')


import basic
from tkinter import *

root = Tk()


Button(root, text="Print the Dictionary from JSON", command=basic.abc).pack()


root.mainloop()


'''\
bs4=Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser
to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers
hours or days of work.
'''

import urllib.request
import html5lib
import bs4 as bs
import ssl

import markup as markup

soup_object= bs.BeautifulSoup(markup, 'html-parser')
from django.utils import html

soup = bs.BeautifulSoup(html, "lxml")
ssl._create_default_https_context = ssl._create_unverified_context

sauce = urllib.request.urlopen('https://stackoverflow.com/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

for s in soup.find_all('a'):
    print(s.string)

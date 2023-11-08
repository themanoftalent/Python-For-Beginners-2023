from bs4 import BeautifulSoup
import urllib
import urlopen
import ssl
from IPython.display import Image
Image('http://www.openbookproject.net/tutorials/getdown/css/images/lesson4/HTMLDOMTree.png')

ssl._create_default_https_context = ssl._create_unverified_context
from django.conf.locale import bs

sauce = urllib.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
#print( type(soup))
print (soup.prettify()[0:1000])


# This restores the same behavior as before.
context = ssl._create_unverified_context()
urllib.urlopen("https://no-valid-cert", context=context)

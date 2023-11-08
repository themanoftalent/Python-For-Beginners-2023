import bs4 as bs
import urllib.request
import urlopen
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()
urllib.urlopen("https://no-valid-cert", context=context)


sauce = urllib.request.urlopen('https://stackoverflow.com/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
for s in soup.find_all('a'):
    print(s.string);kkk


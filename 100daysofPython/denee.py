

import bs4 as bs
import requests

sauce = requests.get('https://stackoverflow.com/')
soup = bs.BeautifulSoup(sauce.content, 'lxml')
for s in soup.find_all('a'):
    print(s.string)

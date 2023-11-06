import re

text = 'We are writing something : meaningless here to search'
matching = re.search('\w{10}', text) #bir cok double w yazmak yerine {rakam yazmak da} olur
we_search = re.search('\w{5}',input('Enter a text'))
if matching:
    print('Found', matching.group())
else:
    print('Nothing found')
if we_search:
    print('Found', we_search.group())
else:
    print('Nothing found')


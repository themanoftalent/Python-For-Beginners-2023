# Using type-specific formatting:


import datetime

d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('Year buyuk, month ve day kucuk, saat dakika saniye buyuk harf :','{:%Y-%m-%d %H:%M:%S}'.format(d))

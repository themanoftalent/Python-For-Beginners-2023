import time


seconds = time.time()
print(seconds)
print()


localtime = time.localtime(seconds)
print(localtime)
print()
print(localtime.tm_year)
print()
print(localtime.tm_mon)
print()
print(localtime.tm_mday)
print()

# asctime = time.asctime(localtime)
# print(asctime)
# strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
# print(strtime)
# mydate = time.strptime('2018-1-1', '%Y-%m-%d')
# print(mydate)
# print()



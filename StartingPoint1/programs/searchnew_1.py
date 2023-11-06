#
# ## Search for pattern 'iii' in string 'piiig'.
# ## All of the pattern must match, but it may appear anywhere.
# ## On success, match.group() is matched text.
# match = re.search (r'iii', 'piiig') = > found, match.group () == "iii"
# match = re.search (r'igs', 'piiig') = > not found, match == None
#
# ## . = any char but \n
# match = re.search (r'..g', 'piiig') = > found, match.group () == "iig"
#
# ## \d = digit char, \w = word char
# match = re.search (r'\d\d\d', 'p123g') = > found, match.group () == "123"
# match = re.search (r'\w\w\w', '@@abcd!!') = > found, match.group () == "abc"

studs = [
    [25, 'Ali Kaya'],
    [126, 'Veli Yaman'],
    [47, 'Cemal Yazan'],
    [58, 'Hakan Arman']
]

del studs[0]

for m in studs:
    print (m)

name = int (input ('Enter a number :'))

for n in studs:
    if name == studs[0]:
        print ('Found')
    print ('Teh found number is ', studs[0])
    break
else:
    print ('The entry not found')

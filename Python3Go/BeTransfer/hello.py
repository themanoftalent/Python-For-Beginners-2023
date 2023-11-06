#edited for python 3 and some basic arrangments
#!editor :Barish

name = str(input('What is your name?\n'))
print ('Hi, %s.' % name)

if name.startswith('A'):
    print('You seem to be lucky')
elif name.startswith('h') and name.endswith('g'):
    print('You look turkish')
else:
    print('No racism, Just coding ')

# 'ab' is short for 'a'ddress'b'ook
print('Dictionaries\n')
ab = {
    'Anna': 'Anna@gmail.com',
    'Larrisa': 'larrisa@hotmail.org',
    'Matt': 'matt@yahoo.com',
    'Bad boy': 'badboy@hotmail.com'
}

print("Anna's address is", ab['Anna'])

# Deleting a key-value pair
del ab['Matt']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Malek'] = 'malek@icloud.com'

if 'Malek' in ab:
    print("\nMalek's address is", ab['Malek'])

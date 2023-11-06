# 'ab' is short for 'a'ddress'b'ook

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# Deleting a key-value pair
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
print("Printing all names and addresses\n\t")
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'
print("\nChecking if :")
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

#elif ab['mudo':'mudeo@judo.com'] not in ab:
    #print(ab.get('mudo'))
    #print('Mudo does not exist', ab['mudo'])

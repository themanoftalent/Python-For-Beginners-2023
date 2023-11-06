elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

for element in elements:
    print(element)

print('*'*23)

print(elements['hydrogen'])

print(elements.get('helium'))

print(elements.get('unobtainium', 'There\'s no such element!'))

print(elements.get('Akifium', 'No such element '))
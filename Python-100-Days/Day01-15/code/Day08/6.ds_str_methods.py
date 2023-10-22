# This is a string object
name = 'Annabel'

if name.startswith('Anna'):
    print('Yes, the string starts with "Anna"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') == -1:
    print('No, it doesnt contain the string "war"')

delimiter = '_*_'
mylistem = ['Turkey', 'Russia', 'Greek', 'Malesia']
print(delimiter.join(mylistem))

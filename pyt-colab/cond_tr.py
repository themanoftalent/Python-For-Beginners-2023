# names = ['ahmet', 'cemil', 'meltem']

# for _, name in enumerate(names):
#     print( _, name)
#

# using zipcode

names = ['Peter', 'Clark', 'Wade']
heroes = ['spiderman', 'superman', 'deadpool']

for name, hero in zip(names, heroes):
    print(f'{name} is in real {hero}')

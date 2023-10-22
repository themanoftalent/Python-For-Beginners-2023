# formatter

formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))
print('____________________________________' * 28)
print('We sre using format "{0}{1}{2}" to print out "a b c" : ', '{0}, {1}, {2}'.format('a', 'b', 'c'))
print('We sre using format "{2}{1}{0}" to print out "c b a" :', '{2}, {1}, {0}'.format('a', 'b', 'c'))
print('We sre using format "{0}{1}{0}" to print out "abra cad abra" :',
      '{0}{1}{0}'.format('abra', 'cad'))  # arguments' indices can be repeated
print('____________________________________' * 28)
print('"Coordinates: {latitude}, {longitude}" latitude="37.24N", longitude="-115.81W" yazildiginda sonuc:',
      'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
print('++++++++++++++++veya++++++++++++++++')

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('**coord gibi birden fazla arg alan bir keywords yazilirsa :',
      'Coordinates: {latitude}, {longitude}'.format(**coord))  # birden fazla parameter almasi gerekmektedir

print('____________________________________' * 28)

print('{:<130}'.format('left aligned'))
# 'left aligned                  '
print('{:>130}'.format('right aligned'))
# '                 right aligned'
print('{:^130}'.format('centered'))
# '           centered
print('or with asterisks')
print('{:*^130}'.format('centered'))  # use '*' as a fill char
# '***********centered***********'

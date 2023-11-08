# Replacing %+f, %-f, and % f and specifying a sign:


print('{:+f}; {:+f}'.format(3.14, -3.14))  # show it always
# '+3.140000; -3.140000'
print('{:f}; {: f}'.format(3.14, -3.14))  # show a space for positive numbers
# ' 3.140000; -3.140000'
print('{:-f}; {:-f}'.format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}'
# '3.140000; -3.140000'

print('{:*^100};{:f}; {: f}'.format('centered', 3.14, -3.14))

print('\nUsing the comma as a thousands separator:')
print('{:,}'.format(1234567890))
# '1,234,567,890'


anumber = 12345678912345678901234567890123456789012345678901234567890123456789012345678901234567891234567890123456789012345678901234567890123456789012345678901234567890

print('{:,}'.format(anumber))

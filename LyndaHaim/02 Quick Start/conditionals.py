#!/usr/bin/python3
# we use meaningful variable names instead of a,b or x

# # number[0], number[1] = 5, 1 lets take input
# # number[0] = int ( input ( "Enter number 1 " ) )
# # number[1] = int ( input ( "Enter number 2 " ) )
# 
# """num = []
# for i in xrange(1, 10):
#     num.append(raw_input('Enter the %s number: '))
# 
# print num"""
# 
# a,b= map(input().split())

number = {} #storing the data

for i in range(2):
    number.update({i: int(input('Enter number {}:'.format(i)))}) #Tamda aradığım şey

if number[0] < number[1]:
    print ( 'number[0] ({}) is less number[1] ({})'.format ( number[0], number[1] ) )
elif number[0] == number[1]:
    print ( 'number[0] ({}) is equal to number[1] ({})'.format ( number[0], number[1] ) )
elif number[0] >= number[1]:
    print ( "number 1 ({}) is greater or equal to number 2 ({})".format ( number[0], number[1] ) )
else:
    print (
        'number[0] ({}) is not less than number[1] ({})'.format ( number[0], number[1] ) )


# print ( "\nExample of a tertiary conditional statement" )
# print ( "foo" if number[0] < number[1]
#         else "with foo number[0] is less than number[1]" )
love="www.stackoverflow.com"
print("\nI love {}".format(love))

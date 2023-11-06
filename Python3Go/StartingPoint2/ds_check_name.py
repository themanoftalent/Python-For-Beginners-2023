def nameAlexSema(Aname, Sname):
    name = input ('What is your name ? ')
    return name


check = nameAlexSema ('Alex', 'Sema')
#print ('your name is ' + str (check))


if str (check)=='Alex' or 'Sema':
    print('Hello %s, I know your name' % str(check))
else:
    print(' The name you input is  '+ str(check))


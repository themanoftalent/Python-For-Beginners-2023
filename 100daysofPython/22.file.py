# f = open('readWrite.txt')
# texttoread = f.read()
# f.close()
#
# print(texttoread)

with open('readWrite.txt', 'r') as fobj:
    text1read = fobj.read()

    print(text1read)

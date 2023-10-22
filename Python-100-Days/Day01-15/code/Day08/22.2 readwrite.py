# first lets create a file
f = open('NewReadFile.txt', 'w+')
for i in range(20):
    f.write("Lets start new life %d\r\n" % (i + 1))
f.close()

# now lets read it
f = open('NewReadFile.txt', 'r')
content = f.read()
print(content)

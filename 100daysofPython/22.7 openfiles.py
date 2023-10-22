file = open("testfile.txt", "w")

file.write("Hello World\t")
file.write('This is our new text file\t')
file.write('and this is another line.\t')
file.write('Why? Because we can.')

file.close()

f=open("testfile.txt", "r")
cont=f.read()
print(cont)
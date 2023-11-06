f = open("straight_linez.txt","r")
#first line is useless
f.readline()
x = []
y = []
z = []
for line in f:
    line = line.replace("\n","").replace("\t"," ").split(" ")
    x.append(line[0])
    y.append(line[0])
    z.append(line[2])
print float(max(z))-float(min(z))

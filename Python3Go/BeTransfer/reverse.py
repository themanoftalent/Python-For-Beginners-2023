a = "Jabba Laci"
li = []
li.extend(a)
print li
size = len(li)
for i in range(0,size/2):
    li[i], li[size-1-i] = li[size -1-i], li[i]
print li


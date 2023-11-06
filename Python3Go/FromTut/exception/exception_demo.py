try:
    f=open("testt.txt")
    for line in f.readlines():
        print(line, end=" ")
except Exception as e:
    print("Error ",e)
print("normal flow")
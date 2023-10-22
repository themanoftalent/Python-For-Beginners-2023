
with open("camelot.txt",'w') as f:
    for i in range(100):
        f.write("We're the knights of the round table We dance whenever we're able"+str(i))



with open("camelot.txt",'r') as f:
    for line in f:
        print(line)
        break



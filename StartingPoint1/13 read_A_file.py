
with open("camelot.txt",'a+') as f:
    f.write("We're the knights of the round table We dance whenever we're able")



with open("camelot.txt",'r') as f:
    for line in f:
        print(line)
        break



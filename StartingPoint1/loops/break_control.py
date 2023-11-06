for s in "test string":
    if s=='s': break
    print(s,end=" ");
else:
    print("else block")
print("normal flow")

a=0
while a<10:
    a+=1
    if a%2==0: break
    print(a)
else:
    print("else block")
print("normal flow")
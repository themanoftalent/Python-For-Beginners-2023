listem=(1,2,3,4,5,6,1)

for n in listem:
    print(n)

print('----'*8)
print('It tells us how many One has been used',listem.count(1))
print(listem.count('Ali'))
print('----'*8)


if 9 not in listem:
  listem.add(9)
if 7 not in listem:
  listem.add(7)
if 6 not in listem:
    listem.add(6)

listem = sorted(listem)

print(listem)
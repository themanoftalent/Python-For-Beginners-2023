# print(list(range(0,100,20)))
#
#
# for item in [0,20,40,60][:3]:
#     print(item)

#=================================
ids=['B3','\nB4','\nB5','\nB6']

with open('ids.txt','w') as f:

    for item in ids:
        f.write(item)

with open('ids.txt','r') as fs:
   line=fs.read()
   for line in ids:
       print(line)
#=================================

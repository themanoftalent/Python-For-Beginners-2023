colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

del colors[4]

colors.remove("blue")

colors.pop(3)

colors.append('white')

colors.sort() #siralama yaildi

print(colors)

if colors[1]!='pink':
    colors.append('pink')
    print(colors)

var='purple'

if not var in colors:
    colors.append(var)
    print(colors)




hello_world = "Hello, World!"

for ch in hello_world:    # print each character from hello_world
    print(ch)

length = 0      # initialize length variable

for i in hello_world:
    length += 1     # add 1 to the length on each iteration

print(len(hello_world) == length)

print(len(hello_world))

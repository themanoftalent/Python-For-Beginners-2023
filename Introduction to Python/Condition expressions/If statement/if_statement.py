name = "John"
age = 17

if name == "John" or age == 17:   # check that name is "John" or age is 17. If so print next 2 lines.
    print("name is John")
    print("John is 17 years old")

tasks = ["task1", "task2"]    # create new list

if len(tasks) == 0 :
    print("empty")
else:
    print('tasks is full')
    print(tasks[0])
print()
for i in tasks:
    print(i)

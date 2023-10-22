import numpy as np

numbers = [12.2, 34.32, 34.5, 198.54, 56, 44, 321, 789, 654, 90]

np_look = np.array(numbers)

print(np_look)
print()
# now we create lbs
np_look_lbs = np_look // 4

print(np_look_lbs)

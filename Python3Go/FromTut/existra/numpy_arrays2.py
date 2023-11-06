look = [12.2, 34.32, 34.5, 198.54, 56, 44, 321, 789, 654, 90]

import numpy as np

np_look = np.array (look)

# now we create lbs
np_look_lbs = np_look // 4 ** 2

print (np_look_lbs)

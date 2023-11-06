# Create 2 new lists height and weight
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array (height)
np_weight = np.array (weight)

print (np_height)
print (np_weight)
print (type (np_weight))  # type numpy.ndarray

# --------------------------------------
# Calculate bmi
bmi = np_weight / np_height ** 2
bim = np_height / np_weight ** 2
# Print the result
print ('np_weight / np_height ** 2 =', bmi)

print ('np_height / np_weight ** 2 =', bim)


# For a boolean response
print('For a boolean response :',bmi > 23)

# Print only those observations above 25
print('Print only those observations above 25 :',bmi[bmi > 25])
import  matplotlib.pyplot as plt
import numpy as np


x1 = np.array([1,2,3])
y1 = np.array([5,5,6])
x2 = np.array([4,7,6])
y2 = np.array([5,6,9])

plt.stackplot(x1, y1)
plt.bar(x2, y2, label="2", color='g')
plt.title('This is matplotlib tutorial')

plt.xlabel('X -axis')
plt.ylabel('Y -axis')

plt.legend()
plt.show()

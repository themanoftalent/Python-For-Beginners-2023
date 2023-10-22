import numpy as np

print('Printing np array: ', np.array([1, 2, 3, 4, 5]))

a = np.array([[-1, 2], [2, -5], [7, 5]])

b = np.array([[2, 4], [6, 9]])

print('Printing shape: ', a.shape)

print('Printing reshape', a.reshape(2, 3))

print('Printina ravel ', a.ravel())

print('Printing zeros  ', np.zeros([2, 3]))
print('Printing ones ', np.ones([2, 3]))

print('Ptinting np round doesnt see the rest ', np.round(23, 998))

nompy = np.pi
print('Printing pi : ', nompy)

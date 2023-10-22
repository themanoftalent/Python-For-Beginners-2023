import numpy as np

x = np.array([[1, 2, 3]]).T
xt_carpim = x.T
print(x.shape)

print(xt_carpim.shape)
print('=========================')
double_olsun = np.array([[-3, -9], [2, 5]])  # double array olmak zorunda sadece -9 da olur
xb = np.array([[1, 2, 3, 4, 5, 6]]).T
xp = np.shape(xb)
xc = np.linalg.det(double_olsun)
xf=np.linalg.inv(double_olsun)
xg=np.linalg.eig(double_olsun)

print(xp)
print('=========================')
print(xb)
print('=========================')
print(xc)
print('=========================')
print(xf)
print('========================='*5)
print(xg)

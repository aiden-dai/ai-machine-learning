import numpy as np

x = np.arange(16)
x = x.reshape(4, 4)
print(x)
print(x.shape[0])
print(x.shape[1])

print(x[:, 0])  # [ 0  4  8 12]

print(x[0, :])  # [0 1 2 3]

print(x[0, 0] + x[1, 0] + x[2, 0] + x[3, 0])

print(np.sum(x, axis=0))  # [24 28 32 36] ,axis=0:  column
print(x[0, :] + x[1, :] + x[2, :]+x[3, :])

print(np.sum(x, axis=1))  # [ 6 22 38 54] , axis=1:  row
print(x[:, 0] + x[:, 1] + x[:, 2]+x[:, 3])

print('*'*20)

y = x[:][np.newaxis]
print(y)
print(y.shape)

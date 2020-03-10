import numpy as np
print(np.__version__)


a = np.array([1, 2, 3, 4])
print(a.dtype)
print(a.ndim)
print(a.shape)
print(len(a))
print(a)


b = a[0:2]
b[0] = 10
print(a)
print(b)


c = np.array([1, 2, 3, 4], dtype=float)
print(c)


# arrange(start, end, step),  >= start, < end
a = np.arange(10)  # not including 10
print(a)
print(b)


# linspace(start, end, n-points), >= start,  <= end
c = np.linspace(0, 10, 5)  # including 10
print(c)


# ones(), zeros(),  eye()
i = np.ones((3, 3))
j = np.zeros((3, 3))
k = np.eye(3)
print(i)
print(j)
print(k)


# random
np.random.seed(100)
m = np.random.rand(4)  # uniform in [0, 1]
n = np.random.randn(4)  # Gaussian
# o = np.random.randint(4)  ?
print(m)
print(n)


a = np.array([1, 2, 3, 4])
print(a)
print(a.reshape(-1, 1))

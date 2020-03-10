import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)

x = np.arange(5)
x_labels = ['a', 'b', 'c', 'd', 'e']
y1 = np.random.randint(3, 10, 5)
y2 = np.random.randint(1, 7, 5)


print(x)
print(y1)
print(y2)

plt.subplot(2, 1, 1)
plt.bar(x, y1, width=0.5)
plt.bar(x, y2, width=0.5, bottom=y1)
plt.xticks(x, x_labels)


plt.subplot(2, 1, 2)
plt.barh(x, y1)
plt.barh(x, y2, left=y1)
plt.yticks(x, x_labels)


plt.show()

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6, 6))

x = np.linspace(0, 2, 30)


plt.subplot(221)
plt.plot(x, x, 'ro')
plt.subplot(222)
plt.plot(x, x ** 2, 'b^')
plt.subplot(223)
plt.plot(x, x ** 3, 'gs')
plt.subplot(224)
plt.plot(x, x * 2 + 5, 'r--')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
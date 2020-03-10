import numpy as np
import matplotlib.pyplot as plt


mean = 0
sigma = 1

x = mean+sigma*np.random.randn(1000)

plt.subplot(211)
plt.hist(x, 20, normed=1, histtype='bar')
plt.subplot(212)
plt.hist(x, 20, normed=1, histtype='bar', cumulative=True, rwidth=0.8)


plt.show()

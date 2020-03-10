import matplotlib.pyplot as plt

x = [30, 10, 25, 35]
x_labels = ['a', 'b', 'c', 'd']

plt.subplot(211)
plt.pie(x, labels=x_labels)


plt.subplot(212)
explode = (0, 0.1, 0, 0)
plt.pie(x, explode=explode, labels=x_labels, shadow=True, startangle=90)


plt.show()

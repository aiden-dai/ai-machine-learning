import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris', data_home='data')

print(iris.head(5))

# fig, axes = plt.subplots(1, 2)

#sns.regplot(x='sepal_length',y='petal_length',data=iris, ax=axes[0])
# sns.lmplot(x='sepal_length',y='petal_length',hue='species',data=iris)
sns.lmplot(x='sepal_length', y='petal_length', col='species', data=iris)

plt.show()

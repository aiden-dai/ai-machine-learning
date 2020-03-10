import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic', data_home='data')

print(titanic.sample(10))

fig, axes = plt.subplots(3, 2)

# sns.barplot(x='class',y='survived',data=titanic)
sns.barplot(x='class', y='survived', data=titanic, ax=axes[0][0])
sns.barplot(x='class', y='survived', hue='sex', data=titanic, ax=axes[0][1])


age1 = titanic['age'].dropna()

sns.distplot(age1, ax=axes[1][0])
sns.distplot(age1, kde=False, ax=axes[1][1])


plt.show()

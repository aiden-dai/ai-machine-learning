import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris', data_home='data')

print(iris.head(5))

# g = sns.PairGrid(iris)
g = sns.pairplot(iris, hue="species")
# g.map_diag(plt.hist)
# g.map_offdiag(plt.scatter)
# g.add_legend()


# g.map_diag(sns.kdeplot)
# g.map_offdiag(sns.kdeplot, n_levels=6)


plt.show()

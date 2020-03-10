import numpy as np
import pandas as pd

# read_csv
titanic = pd.read_csv('data/titanic.csv', sep = ',', header = 0)

# columns are Series Object

age = titanic.age
# or age = titanic['age']
print(type(age))  # <class 'pandas.core.series.Series'>

# Series.values
print(age[:3].values)  # [22. 38. 26.]


# Rows are still DataFrame Object
row1 = titanic[:1]
print(type(row1))  # <class 'pandas.core.frame.DataFrame'>


# Slices are also DataFrame Object
s1 = titanic.loc[:5, ['survived', 'sex']]
print(s1)
print(type(s1))  # <class 'pandas.core.frame.DataFrame'>


# iloc[i] is Row[i], but a Series object

s2 = titanic.iloc[0]
print(type(s2))  # <class 'pandas.core.series.Series'>
print(s2)



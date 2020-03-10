import numpy as np
import pandas as pd

# read_csv
titanic = pd.read_csv('data/titanic.csv', sep = ',', header = 0)

# Grouping
s1 = titanic.groupby('sex').sum()
# titanic.groupby(['sex']).sum()  # all columns
# titanic.groupby(['sex']).count()  # all columns

print(s1)
print(type(s1))  # <class 'pandas.core.frame.DataFrame'>

s2 = titanic.groupby(['sex']).size()  # sum of grouped by columns
print(s2)
print(type(s2))  # <class 'pandas.core.series.Series'>
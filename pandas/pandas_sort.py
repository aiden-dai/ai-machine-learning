import numpy as np
import pandas as pd

# read_csv
titanic = pd.read_csv('data/titanic.csv', sep=',', header=0)

# Sorting
# it doesn't change the dataframe
titanic.sort_values(by='survived', ascending=True)
print(titanic.head(5))

titanic = titanic.sort_values(by=['survived', 'age'], ascending=True)
print(titanic.head(5))

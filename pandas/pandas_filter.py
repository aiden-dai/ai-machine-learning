import numpy as np
import pandas as pd

# read_csv
titanic = pd.read_csv('data/titanic.csv', sep = ',', header = 0)

# Filter
s5 = titanic[titanic.sex == 'male']
print(s5.head())

s6 = titanic[titanic.sex.isin(['male'])]
print(s6.head())
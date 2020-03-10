import numpy as np
import pandas as pd

# read_csv
titanic = pd.read_csv('data/titanic.csv', sep=',', header=0)

print(titanic.head())

titanic_small = titanic.iloc[:5, [0, 1, 2]]

print(titanic_small.head())

# aggfunc by default is mean
titanic_pivot = pd.pivot_table(titanic_small, index=['sex'],  columns=[
                               'pclass'], values='survived', aggfunc='count', fill_value=0)
print(titanic_pivot.head(5))

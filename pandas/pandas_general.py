import numpy as np
import pandas as pd

print(pd.__version__)


# read_csv as a DataFrame
titanic = pd.read_csv('data/titanic.csv', sep = ',', header = 0)

print(type(titanic))  # <class 'pandas.core.frame.DataFrame'>

print(titanic.head(5))

# Check columns
print(titanic.columns)

# check index
print(titanic.index)

# check dtypes of columns
print(titanic.dtypes)

# use info() to summary data
print(titanic.info())

# describe() shows a quick statistic summary of your data:
print(titanic.describe())


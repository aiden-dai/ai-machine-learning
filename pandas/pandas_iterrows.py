import numpy as np
import pandas as pd

# read_csv
titanic = pd.read_csv('data/titanic.csv', sep = ',', header = 0)

titanic = titanic[:5]

for i, row in titanic.iterrows():
    # print(type(row))  # <class 'pandas.core.series.Series'>
    print('Row {0},  Sex: {1.sex}, Survived: {1.survived}'.format(i, row))
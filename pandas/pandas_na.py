import numpy as np
import pandas as pd

# read_csv
titanic = pd.read_csv('data/titanic.csv', sep=',', header=0)

# Handle N/A
# dropna, fillna doesn't change the objects
titanic.dropna(how='any')
# titanic.fillna(value=0)
print(titanic.head(5))

import numpy as np
import pandas as pd

data = pd.read_csv('data/brain_size.csv', sep=';', na_values=".")
print(data)
print(data.shape)
print(data.columns)


print(data['Gender'])

viq_mean = data[data['Gender'] == 'Female']['VIQ'].mean()
print(viq_mean)

groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['VIQ']:
    print((gender, value.mean()))

print(groupby_gender.mean())

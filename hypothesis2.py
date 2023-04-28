import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import imageio
import os

df = pd.read_csv(r'data.csv')
df=df.drop(['Timestamp'], axis=1)
df=df[df['Physical activity']<=50]
df=df[df['Sleep time']<=12]
df=df[df['Eating outside']<=90]
df=df[df['money on food per day']<=1000]

df1 = (df[df['Physical activity']<=2])
df2 = (df[df['Physical activity']>2])
n_inac = len(df1.index)
n_ac = len(df2.index)
data_inac = df1.to_numpy()
data_ac = df2.to_numpy()

slp_inac = np.sort(data_inac[:,3])
slp_ac = np.sort(data_ac[:,3])

print(len(slp_inac))
print(len(slp_ac))

std_inac = np.var(slp_inac)
std_ac = np.var(slp_ac)

print('std_inac:  ', std_inac)
print('std_ac:  ',std_ac)

print('mean_inac:  ',np.sum(slp_inac)/len(slp_inac))
print('mean_ac:  ', np.sum(slp_ac)/len(slp_ac))

print('f:  ', std_ac/std_inac)


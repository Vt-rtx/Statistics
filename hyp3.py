import numpy as np
import pandas as pd

df = pd.read_csv(r'Effects of food habits on daily life.csv')
df=df.drop(['Timestamp'], axis=1)
df=df[df['Physical activity']<=50]
df=df[df['Sleep time']<=12]
df=df[df['Eating outside']<=90]
df=df[df['money new']<=1000]

lunch = df[df['BLD'] == 'Lunch']  #45
non_lunch = df[df['BLD'] != 'Lunch']  #188
lunch_with_nap = df[(df['BLD'] == 'Lunch')&(df['afternoon nap'] == 'Yes')]  #24
non_lunch_with_nap = df[(df['BLD'] != 'Lunch')&(df['afternoon nap'] == 'Yes')] #96

print(lunch_with_nap)
print(non_lunch_with_nap)
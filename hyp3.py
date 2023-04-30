import numpy as np
import pandas as pd

df = pd.read_csv(r'Effects of food habits on daily life.csv')
df=df[df['Physical activity']<=50]
df=df[df['Sleep time']<=12]
df=df[df['Eating outside']<=90]
df=df[df['money on food per day']<=1000]

lunch = df[df['BLD'] == 'Lunch']  #39
non_lunch = df[df['BLD'] != 'Lunch']  #173
lunch_with_nap = df[(df['BLD'] == 'Lunch')&(df['afternoon nap'] == 'Yes')]  #19
non_lunch_with_nap = df[(df['BLD'] != 'Lunch')&(df['afternoon nap'] == 'Yes')] #89

print(lunch_with_nap)
print(non_lunch_with_nap)
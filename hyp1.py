import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\prana\OneDrive\Desktop\IITHyderabad\codes\Statistics\Effects of food habits on daily life.csv")
df=df.drop(['Timestamp'], axis=1)
df=df[df['Physical activity']<=50]
df=df[df['Sleep time']<=12]
df=df[df['Eating outside']<=90]
df=df[df['money new']<=1000]

veg = df[df['FC'] == 'Vegetarian']
nonveg = df[df['FC'] != 'Vegetarian']

print(nonveg.describe())
print()
print(veg.describe())





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def normal(x,mu,sigma):
    return 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-((x-mu)/sigma)**2)

df = pd.read_excel(r'Effects of food habits on daily life (Responses).xlsx')
df=df.drop(['Timestamp','Did the keyword "18+" affect your decision in choosing to fill this form?'], axis=1)
df=df[df['Physical activity']<=50]
df=df[df['Sleep time']<=12]
df=df[df['Eating outside']<=90]
df=df[df['money on food per day']<=1000]

data=df.to_numpy()
# print(data)

physicalactivity=data[:,1]

sleeptime=data[:,2]
eatoutfrequency=data[:,3]
for i in range(data[:,4].shape[0]):
    if(data[:,4][i]>=500):
        data[:,4][i]=data[:,4][i]/30
moneyspent=data[:,4]


#Histograms
counts,edges,bars=plt.hist(physicalactivity,bins=range(0,51,2))
plt.xlabel('Physical activity per week in hours')
plt.ylabel('Count')
plt.bar_label(bars)
plt.grid()
plt.show()
counts,edges,bars=plt.hist(sleeptime,bins=range(0,14))
plt.bar_label(bars)
plt.xlabel('Sleep time in hours per day')
plt.ylabel('Count')
plt.grid()
plt.show()
counts,edges,bars=plt.hist(eatoutfrequency,bins=range(0,91,3))
plt.bar_label(bars)
plt.xlabel('Number of times a student eats outside per month')
plt.ylabel('Count')
plt.grid()
plt.show()
counts,edges,bars=plt.hist(moneyspent,bins=range(0,500,40))
plt.bar_label(bars)
plt.xlabel('Money spent on food per day')
plt.ylabel('Count')
plt.grid()
plt.show()

#Boxplots
veg=[]
Nonveg=[]
Egg=[]
for i in range(data.shape[0]):
    if(data[i][0]=='Non-vegetarian'):
        Nonveg.append(data[i])
    elif(data[i][0]=='Vegetarian'):
        veg.append(data[i])
    else:
        Egg.append(data[i])

veg=np.array(veg) 
Nonveg=np.array(Nonveg) 
Egg=np.array(Egg)  
color=['red','green','brown']
for i in range(1,5):
    temp=[veg[:,i],Nonveg[:,i],Egg[:,i]]
    plt.boxplot(temp)
    plt.xticks([1,2,3],["Veg","Nonveg","Egg"])
    plt.grid()
    plt.show()

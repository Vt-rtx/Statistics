import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import imageio
import os

def gif(path,name):
    files=os.listdir(f'{path}')
    image_path=[os.path.join(f'{path}',file) for file in files]
    images=[]
    for img in image_path:
        images.append(imageio.imread(img))
    imageio.mimwrite(f'CLT/{name}.gif',images,fps=5)

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
columns=['Physical activity per week in hours','Sleep time in hours per day','Number of times a student eats outside per month','Money spent on food per day']
veg=np.array(veg) 
Nonveg=np.array(Nonveg) 
Egg=np.array(Egg)  
colors=['green','red','brown']
for i in range(1,5):
    temp=[veg[:,i],Nonveg[:,i],Egg[:,i]]
    # Create the boxplot
    fig, ax = plt.subplots()
    box = ax.boxplot(temp, patch_artist=True, vert=True)
    # Set the xticks and labels
    xticks = [1, 2, 3]
    xticklabels = ['Veg', 'Non-veg', 'Veg+Egg']
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
    ax.set_ylabel(columns[i-1])
    # Set the facecolor of each box
    for i, patch in enumerate(box['boxes']):
        patch.set_facecolor(colors[i])
    plt.grid()
    plt.show()


#CLT
pairs = []
mu=[]
ks=range(2,50)
for k in ks:
    for i in range(1,200):
        sleeptime1=list(sleeptime)
        for p in range(len(sleeptime) // k):
            sum=0
            for j in range(k):
                sum+=sleeptime1.pop(random.randrange(len(sleeptime1)))
            mu.append(sum/k)
    # print(len(pairs))
    mu.sort()
    unique_mu=list(set(mu))
    # print(unique_mu)
    freq=[]
    for i in range(len(unique_mu)):
        freq.append(mu.count(unique_mu[i])/len(mu))
    fig1, ax1= plt.subplots()
    ax1.grid()
    plt.xlim(right=13)
    plt.ylim(top=0.2)
    ax1.scatter(unique_mu,freq,label=f'n={k}')
    ax1.legend()
    plt.savefig(f'CLT\{k:003}',dpi=100,facecolor='white')
gif('CLT','CLT')

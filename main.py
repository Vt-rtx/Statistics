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
df=df.drop(['Timestamp'], axis=1)
df=df[df['Physical activity']<=50]
df=df[df['Sleep time']<=12]
df=df[df['Eating outside']<=90]
df=df[df['money on food per day']<=1000]

data=df.to_numpy()
# print(data)

physicalactivity=np.sort(data[:,1])
#Central tendencies for physical activity 
print('Central tendencies for physical activity')
count=physicalactivity.shape[0]
max=np.max(physicalactivity)
std=np.sqrt(np.var(physicalactivity))
min=np.min(physicalactivity)
q1=physicalactivity[int(count/4)]
q2=physicalactivity[int(count/2)]
q3=physicalactivity[int(3*count/4)]
mean=np.mean(physicalactivity)
print(f' count = {count}\n mean = {mean}\n std = {std}\n max = {max}\n min = {min}\n 25% = {q1}\n 50% = {q2}\n 75% = {q3}')

sleeptime=np.sort(data[:,2])
#Central tendencies for sleep time
print('Central tendencies for sleep time')
count=sleeptime.shape[0]
max=np.max(sleeptime)
std=np.sqrt(np.var(sleeptime))
min=np.min(sleeptime)
q1=sleeptime[int(count/4)]
q2=sleeptime[int(count/2)]
q3=sleeptime[int(3*count/4)]
mean=np.mean(sleeptime)
print(f' count = {count}\n mean = {mean}\n std = {std}\n max = {max}\n min = {min}\n 25% = {q1}\n 50% = {q2}\n 75% = {q3}')

eatoutfrequency=np.sort(data[:,3])
#Central tendencies for number of time eat out in a month
print('Central tendencies for number of times eat out in a month')
count=eatoutfrequency.shape[0]
max=np.max(eatoutfrequency)
std=np.sqrt(np.var(eatoutfrequency))
min=np.min(eatoutfrequency)
q1=eatoutfrequency[int(count/4)]
q2=eatoutfrequency[int(count/2)]
q3=eatoutfrequency[int(3*count/4)]
mean=np.mean(eatoutfrequency)
print(f' count = {count}\n mean = {mean}\n std = {std}\n max = {max}\n min = {min}\n 25% = {q1}\n 50% = {q2}\n 75% = {q3}')


for i in range(data[:,4].shape[0]):
    if(data[:,4][i]>=500):
        data[:,4][i]=data[:,4][i]/30
moneyspent=np.sort(data[:,4])
#Central tendencies for money spent everyday
print('Central tendencies for money spent everyday')
count=moneyspent.shape[0]
max=np.max(moneyspent)
std=np.sqrt(np.var(moneyspent))
min=np.min(moneyspent)
q1=moneyspent[int(count/4)]
q2=moneyspent[int(count/2)]
q3=moneyspent[int(3*count/4)]
mean=np.mean(moneyspent)
print(f' count = {count}\n mean = {mean}\n std = {std}\n max = {max}\n min = {min}\n 25% = {q1}\n 50% = {q2}\n 75% = {q3}')

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
ks=range(2,40)
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

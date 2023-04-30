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
    imageio.mimwrite(f'{path}/{name}.gif',images,fps=5)

def normal(x,mu,sigma):
    return 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-((x-mu)/sigma)**2)

df = pd.read_csv(r'/home/rutvk/Desktop/Sem4/Stats/Statistics/Effects of food habits on daily life.csv')
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

# #Histograms
# counts,edges,bars=plt.hist(physicalactivity,bins=range(0,51,2))
# plt.xlabel('Physical activity per week in hours')
# plt.ylabel('Count')
# plt.bar_label(bars)
# plt.grid()
# plt.show()
# counts,edges,bars=plt.hist(sleeptime,bins=range(0,14))
# plt.bar_label(bars)
# plt.xlabel('Sleep time in hours per day')
# plt.ylabel('Count')
# plt.grid()
# plt.show()
# counts,edges,bars=plt.hist(eatoutfrequency,bins=range(0,91,3))
# plt.bar_label(bars)
# plt.xlabel('Number of times a student eats outside per month')
# plt.ylabel('Count')
# plt.grid()
# plt.show()
# counts,edges,bars=plt.hist(moneyspent,bins=range(0,500,40))
# plt.bar_label(bars)
# plt.xlabel('Money spent on food per day')
# plt.ylabel('Count')
# plt.grid()
# plt.show()

# #Boxplots
# veg=[]
# Nonveg=[]
# Egg=[]
# for i in range(data.shape[0]):
#     if(data[i][0]=='Non-vegetarian'):
#         Nonveg.append(data[i])
#     elif(data[i][0]=='Vegetarian'):
#         veg.append(data[i])
#     else:
#         Egg.append(data[i])
# columns=['Physical activity per week in hours','Sleep time in hours per day','Number of times a student eats outside per month','Money spent on food per day']
# veg=np.array(veg) 
# Nonveg=np.array(Nonveg) 
# Egg=np.array(Egg)  
# colors=['green','red','brown']
# for i in range(1,5):
#     temp=[veg[:,i],Nonveg[:,i],Egg[:,i]]
#     # Create the boxplot
#     fig, ax = plt.subplots()
#     box = ax.boxplot(temp, patch_artist=True, vert=True)
#     # Set the xticks and labels
#     xticks = [1, 2, 3]
#     xticklabels = ['Veg', 'Non-veg', 'Veg+Egg']
#     ax.set_xticks(xticks)
#     ax.set_xticklabels(xticklabels)
#     ax.set_ylabel(columns[i-1])
#     # Set the facecolor of each box
#     for i, patch in enumerate(box['boxes']):
#         patch.set_facecolor(colors[i])
#     plt.grid()
#     plt.show()


#CLT
ks=range(40,70)
for k in ks:
    pairs = []
    mu=[]   
    for i in range(1,1000):
        sleeptime1=list(sleeptime)
        for p in range(len(sleeptime) // k):
            sum=0
            for j in range(k):
                sum+=sleeptime1.pop(random.randrange(len(sleeptime1)))
            mu.append(sum/k)
    # print(len(pairs))
    mu.sort()
#This part of code shows histogram rep for CLT
    fig1, ax1= plt.subplots()
    counts,edges,bars=ax1.hist(mu,bins=np.linspace(1,13,100),label=f'n={k}')
    plt.xlim(right=4,left=8)
    plt.grid()
    plt.legend()
    plt.xlim(left=6,right=8)
    plt.ylim(top=1200)
    plt.savefig(f'CLT_histogram\{k:003}',dpi=100,facecolor='white')
gif('CLT_histogram','CLT_histogram')
#This part of code show points for CLT
#     unique_mu=list(set(mu))
#     # print(unique_mu)
#     freq=[]
#     for i in range(len(unique_mu)):
#         freq.append(mu.count(unique_mu[i])/len(mu))
#     fig1, ax1= plt.subplots()
#     ax1.grid()
#     plt.xlim(left=6,right=8)
#     plt.ylim(top=0.05)
#     ax1.scatter(unique_mu,freq,label=f'n={k}')
#     ax1.legend()
#     plt.savefig(f'CLT\{k:003}',dpi=100,facecolor='white')
# gif('CLT','CLT')

veg=[]
Nonveg=[]
Egg=[]
for i in range(data.shape[0]):
    if(data[i][0]=='Non-vegetarian'):
         Nonveg.append(data[i])
    elif(data[i][0]=='Vegetarian'):
         veg.append(data[i])
    else:
        veg.append(data[i])
veg=np.array(veg) 
Nonveg=np.array(Nonveg)   
veg = list(veg[:,2])
Nonveg = list(Nonveg[:,2])
m = 10
n = 20
veg_var = []
Nonveg_var = []
points = []
# Verify F distribution for variances of sleep time
for i in range(100):
    #randomly sample a tuple of length m from veg and n from Nonveg\
    veg_sample = random.sample(veg, m)
    Nonveg_sample = random.sample(Nonveg, n)
    veg_var.append(np.var(veg_sample))
    Nonveg_var.append(np.var(Nonveg_sample))
    points.append(np.var(veg_sample)/np.var(Nonveg_sample))
    


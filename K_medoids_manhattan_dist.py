import numpy as np
import pandas as pd
l=[]
a=int(input("Enter number of datapoints : "))
for i in range(a):
    b=int(input(f"Enter {i+1} : "))
    l.append(b)
print("Datapoints : ",l)
print("Number os clusters K =2")
c1=np.random.choice(l)
print("Random 1 : ",c1)
c2=np.random.choice(l)
while c1==c2:
    c2=np.random.choice(l)
print("Random 2 : ",c2)
clus1=[]
clus2=[]
for i in range(a):
    if(l[i]<c1):
        d1=c1-l[i]
    else:
        d1=l[i]-c1
    if(l[i]<c2):
        d2=c2-l[i]
    else:
        d2=l[i]-c2
    if(d1<d2):
        clus1.append(l[i])
    else:
        clus2.append(l[i])
print("Cluster 1 : ",clus1)
print("Cluster 2 : ",clus2)

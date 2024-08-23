
import pandas as pd
import numpy as np
a=int(input("Enter number of data : "))
c=[]
l=[]
for i in range(a):
    b=input("Element : ")
    c.append(b)
for i in range(1,a+1):
    l.append(i)
x=np.array(c)
y=np.array(l)
k=pd.Series(x,index=y)
print(k)
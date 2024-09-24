import pandas as pd
import numpy as np
import math

df=pd.read_csv('Data.csv')
print(df)
age=df["Age"].tolist()
age=[int(i) for i in age]
inc=df["income"].tolist()
inc=[int(i) for i in inc]
cards=df["no. of cards"].tolist()
cards=[int(i) for i in cards]
loan=df["Loan"].tolist()
nage=int(input("Enter Age : "))
ninc=int(input("Enter Income : "))
nc=int(input("Enter number of cards : "))
ec=[]
sa=[] 
si=[]
sc=[]
for i in range(len(age)):
    n=age[i]-nage
    n=n*n
    sa.append(n)
    n=inc[i]-ninc
    n=n*n
    si.append(n)
    n=cards[i]-nc
    n=n*n
    sc.append(n)
    n=math.sqrt(sa[i]+si[i]+sc[i])
    ec.append(n)

print(ec)
df['Eucledian dis']=ec
print(df)
df=df.sort_values('Eucledian dis')
print(df)
k=0
while(k%2==0):
 k=int(input("Enter odd value of k :"))
 if(k%2==0):
     print("Even k Enter again ")
loan=df["Loan"].tolist()
l=[]
for i in range(k):
    l.append(loan[i])
print("3 nearest values : ",l)
c1=0
c2=0;
for i in range(k):
    if(l[i]=='N'):
        c1=c1+1
    else:
        c2=c2+1
if c1>c2:
    nloan='N'
    print("Loan : "+nloan)
else:
    nloan='Y'
    print("Loan : "+nloan) 
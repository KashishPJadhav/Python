import pandas as pd
import numpy as np
import math
from sklearn.linear_model import LinearRegression
df=pd.read_csv('Binary.csv')
x=df.iloc[:,:-1].values
y=df.iloc[:,2:].values
print(x)
print(y)
print(df)
m=LinearRegression()
m.fit(x,y)
yp=m.predict(x)
print(yp)
df['Predicted Y']=yp
t2=df['target'].tolist()
mse=[]
for i in range (len(t2)):
    a=(t2-yp)*(t2-yp)
    mse.append(a)
df['MSE loss']=mse
print(df)
    

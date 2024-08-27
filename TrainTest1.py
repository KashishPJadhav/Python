import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
dataset=pd.read_csv('Mobile-Price-Prediction-cleaned_data.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,:-1].values
xtr,xte,ytr,yte=train_test_split(x,y,test_size=0.2,random_state=0)
r=LinearRegression()
r.fit(xtr,ytr)
yp=r.predict(xte)
plt.scatter(xtr,ytr,color='red',label='Training X')
plt.plot(xtr,r.predict(xtr),color='green',label='Training Y')
plt.title('Training Data')
plt.xlabel('X Training')
plt.ylabel('Y Training')
plt.legend()
plt.show()
plt.scatter(xte,yte,color='blue',label='Testing X')
plt.plot(xte,yp,color='green',label='Testing Y')
plt.title('Testing Data')
plt.xlabel('X Testing')
plt.ylabel('Y Testing')
plt.legend()
plt.show()
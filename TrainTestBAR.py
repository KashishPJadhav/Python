import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
dataset=pd.read_csv('diabetes.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
xtr,xte,ytr,yte=train_test_split(x,y,test_size=0.4,random_state=0)
r=LinearRegression()
r.fit(xtr,ytr)
yp=r.predict(xte)
column_index = 0
#plt.scatter(xtr[:, column_index],ytr,color='red',label='Training X')

# Plot bar chart for the first column of predictions
plt.bar(np.arange(len(xtr)), r.predict(xtr), label='Training Y')
plt.title('Training Data')
plt.xlabel('X Training')
plt.ylabel('Y Training')
plt.legend()
plt.show()

#plt.scatter(xte[:, 0],yte[:, 0],color='blue',label='Testing X') # Select the first column of xte and yte for scatter plot

# Plot bar chart for the first column of predictions
plt.bar(np.arange(len(xte)), r.predict(xte), label='Testing Y')
plt.title('Testing Data')
plt.xlabel('X Testing')
plt.ylabel('Y Testing')
plt.legend()
plt.show()
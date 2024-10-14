import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

n=int(input("Enter number of datapoints : "))

x=[]
y=[]

for i in range(n):
    xv=int(input("X[] : "))
    yv=int(input("Y[] : "))
    x.append([xv])
    y.append([yv])

print(x,y)

model=LinearRegression();
model.fit(x,y)
yp=model.predict(y)
plt.plot(x,y)
plt.scatter(x,yp)
plt.show()

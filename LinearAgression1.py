import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x=np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y=np.array([17,23,35,48,52,66,79,83,96,104])
model=LinearRegression()
model.fit(x,y)
yp=model.predict(x)
beta_0 = model.intercept_
beta_1 = model.coef_[0]
print(f"Intercept (beta_0): {beta_0}")
print(f"Slope (beta_1): {beta_1}")
plt.scatter(x,y,color='brown',label='data')
plt.plot(x,yp,color='black',label='line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

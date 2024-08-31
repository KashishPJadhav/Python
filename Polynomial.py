from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression



poly_features=PolynomialFeatures(degree=2)
data=pd.read_csv('Book1.csv')
x=data['A']
y=data['B']


x_poly=poly_features.fit_transform(x.values.reshape(-1,1))
model=LinearRegression()
model.fit(x_poly,y)
y_predict=model.predict(x_poly)
plt.scatter(x,y,label='Data')
plt.plot(x,y_predict)
plt.show()
plt.legend()


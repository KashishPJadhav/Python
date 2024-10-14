# 1. Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Lasso, Ridge

# 2. Take inputs from user for the dataset
n = int(input("Enter the number of data points: "))

X = []
y = []

print("\nEnter the values for X and y (target variable):")
for i in range(n):
    x_value = float(input(f"Enter X[{i + 1}]: "))
    y_value = float(input(f"Enter y[{i + 1}]: "))
    X.append([x_value])  # Append as a list to form 2D array
    y.append([y_value])  # Append as a list for consistent shape

X = np.array(X)
y = np.array(y)

# 3. Take input for the degree of the polynomial
degree = int(input("\nEnter the degree of the polynomial: "))

# 4. Apply Polynomial Transformation
poly = PolynomialFeatures(degree=degree)
X_poly = poly.fit_transform(X)

# 5. Apply Lasso Regression
alpha_lasso = float(input("\nEnter the alpha value for Lasso Regression (regularization strength): "))
lasso = Lasso(alpha=alpha_lasso)  # L1 regularization
lasso.fit(X_poly, y)
y_pred_lasso = lasso.predict(X_poly)

# 6. Apply Ridge Regression
alpha_ridge = float(input("Enter the alpha value for Ridge Regression (regularization strength): "))
ridge = Ridge(alpha=alpha_ridge)  # L2 regularization
ridge.fit(X_poly, y)
y_pred_ridge = ridge.predict(X_poly)

# 7. Plot the Results
X_plot = np.linspace(min(X), max(X), 100).reshape(100, 1)
X_plot_poly = poly.transform(X_plot)

y_plot_lasso = lasso.predict(X_plot_poly)
y_plot_ridge = ridge.predict(X_plot_poly)

plt.scatter(X, y, color="blue", label="Actual Data", alpha=0.5)
plt.plot(X_plot, y_plot_lasso, color="red", label="Lasso Prediction")
plt.plot(X_plot, y_plot_ridge, color="green", label="Ridge Prediction")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

import pandas as pd
import numpy as np
import math
from sklearn.linear_model import LinearRegression

# Load the data
df = pd.read_csv('Binary.csv')

# Prepare input and target variables
x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values  # Assuming the last column is the target

print("X values:\n", x)
print("Y values:\n", y)
print("Dataframe:\n", df)

# Create and train the model
m = LinearRegression()
m.fit(x, y)

# Make predictions
yp = m.predict(x)
print("Predicted Y values:\n", yp)

# Add predictions to dataframe
df['Predicted Y'] = yp

# Calculate MSE Loss (Logarithmic Loss)
log = []
for i in range(len(y)):
    # Avoid taking log of zero by adding a small constant (epsilon)
    epsilon = 1e-10
    predicted_y = yp[i]
    true_y = y[i]
    loss = - (true_y * math.log(predicted_y + epsilon, 10) +
              (1 - true_y) * math.log(1 - predicted_y + epsilon, 10))
    log.append(loss)

df['Log loss'] = log
print("Dataframe with Predicted Y and MSE Loss:\n", df)

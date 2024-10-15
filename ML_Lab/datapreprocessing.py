import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Original Dataset : \n")
dataset = pd.read_csv('DATA.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values
print(X)
print(Y)
print("\n\n\n")
print("Missing values exchanged with mean : \n")
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy="mean")
imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])
print(X)
print("\n\n\n")
print("Used one hot encoder : \n")
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)
print("\n\n\n")
print("Label Encoder : \n")
from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
Y = LE.fit_transform(Y)
print(Y)
print("\n\n\n")
print("Train Test split : \n")
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)
print(X_train)
print(X_test)
print(Y_train)
print(Y_test)


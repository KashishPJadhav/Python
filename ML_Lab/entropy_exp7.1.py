import pandas as pd
import numpy as np
data = pd.read_csv('iris.csv')

target_column = data.iloc[:, -1] 

value_counts = target_column.value_counts(normalize=True)

entropy = -np.sum(value_counts * np.log2(value_counts))

print(f"Entropy of the target column: {entropy:.4f}")

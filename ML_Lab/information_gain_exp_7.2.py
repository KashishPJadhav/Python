import pandas as pd
import numpy as np
data = pd.read_csv('iris.csv')

target_column = data.iloc[:, -1] 

value_counts = target_column.value_counts(normalize=True)

entropy = -np.sum(value_counts * np.log2(value_counts))

print(f"Entropy of the target column: {entropy:.4f}")
target_col = 'species' 
feature_col = 'sepal_length' 

value_counts_total = data[target_col].value_counts(normalize=True)
total_entropy = -np.sum(value_counts_total * np.log2(value_counts_total))
values = data[feature_col].unique()
weighted_entropy = 0

for value in values:
    subset = data[data[feature_col] == value] 
    value_counts_subset = subset[target_col].value_counts(normalize=True)
    subset_entropy = -np.sum(value_counts_subset * np.log2(value_counts_subset))
    
    
    weighted_entropy += (len(subset) / len(data)) * subset_entropy

info_gain = total_entropy - weighted_entropy

print(f"Information Gain for splitting on '{feature_col}': {info_gain:.4f}")

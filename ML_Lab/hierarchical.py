import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Input the number of data points
data = []
a = int(input("Enter number of datapoints: "))
for i in range(a):
    b = int(input(f"Enter data point {i+1}: "))
    data.append(b)


data = np.array(data).reshape(-1, 1)  

Z = linkage(data, method='single')  


plt.figure(figsize=(8, 4))
dendrogram(Z, labels=data.flatten(), distance_sort='descending')
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Data points")
plt.ylabel("Distance")
plt.show()

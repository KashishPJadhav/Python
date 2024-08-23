import numpy as np
arr=np.array([1,2,3,4])
print(arr)
#data_types
x=np.array([1,2,3,4],dtype=float)
print("np.array([1,2,3,4],dtype=float) : ",x)
#shape of the array
s=np.array([3,2,14,5])
print("s.shape :",s.shape)#it prints the size
#sum of two arrays
arr1=np.array([1,2,5,3,7])
print("arr1 :",arr1)
print("arr1.shape :",arr1.shape)
print("arr1.size :",arr1.size)
arr2=np.array([2,1,4,6,8])
print("arr2 :",arr2)
print("arr1+arr2 : ",arr1+arr2)
#multiplication of 2D array or matrix multiplication
a1=np.array([[1,2],[2,2]])
a2=np.array([[1,5],[3,4]])
print("2D array a1 :\n",a1)
print("a1.shape :",a1.shape)
print("a1.size :",a1.size)
print("2D array a2 :\n",a2)
print("a1 @ a2 :\n",a1 @ a2)
print("a1 + a2 :\n",a1 + a2)
print("a1 - a2 :\n",a1 - a2)
print("a1 * a2 :\n",a1 * a2)

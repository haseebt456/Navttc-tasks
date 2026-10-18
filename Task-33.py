import numpy as np

print("Check the number of dimensions, shape, and size of an array")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)
print("number of dimensions : ", arr.ndim)
print(arr)
print('shape of array :', arr.shape)
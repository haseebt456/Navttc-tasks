import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

print("splitting 1-D array into 3 parts:")
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

print("splitting 2-D array into 3 parts along axis 0:")
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print(arr)
newarr = np.array_split(arr, 3)

print(newarr)
print(newarr[0])
print(newarr[1])   
print(newarr[2]) 

print("splitting 2-D array into 3 parts along axis 1:")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)

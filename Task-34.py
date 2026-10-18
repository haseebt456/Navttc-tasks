import numpy as np

print("Original array:")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr)
print("Reshaped array with 2-dimesions:")
newarr = arr.reshape(4, 3)

print(newarr)
print("Reshaped array with 3 dimensions:")
newarr = arr.reshape(2, 3, 2)

print(newarr)
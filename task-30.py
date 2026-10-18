import numpy as np

print("Slicing 1-d array")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr)
print(arr[1:5])
print("reverse slicing")
print(arr[::-1])
print("Slicing 2-d array")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr)
print("from both rows, return index 2")
print(arr[0:2, 2])
print("from both rows, return index 1 to 4")
print(arr[0:2, 1:4])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
print("Where the elements of the array are equal to 4:")
x = np.where(arr == 4)

print(x)
print("Where the elements of the array are even:")
x = np.where(arr%2 == 0)

print(x)

arr = np.array([6, 7, 8, 9])
print("index where adding elemennt whould maintain the sorted order:")
x = np.searchsorted(arr, 7)

print(x)

x = np.searchsorted(arr, 7, side='right')
print(x)

arr = np.array([1, 3, 5, 7])
print("index where adding elemennt whould maintain the sorted order of the array:")
x = np.searchsorted(arr, [2, 4, 6])

print(x)
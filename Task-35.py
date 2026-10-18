import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("2-D array:")
for x in arr:
  print(x)

print("Iterating 2-D array:")
for x in arr:
  for y in x:
    print(y)
print("Iterating 3-D array:")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

print("Iterating 3-D array with np.nditer:")
for x in np.nditer(arr):
  print(x)

arr = np.array([1, 2, 3])
print("Iterating array with different data types:")
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

print("Iterating array with different step size:")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)

print("Enumerated iteration of an array:")
for idx, x in np.ndenumerate(arr):
  print(idx, x)
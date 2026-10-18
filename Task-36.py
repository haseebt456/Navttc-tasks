import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])
print("Concatenating two 1-D arrays:")
arr = np.concatenate((arr1, arr2))

print(arr)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])
print("Concatenating two 2-D arrays along axis 0:")
arr = np.concatenate((arr1, arr2), axis=0)
print(arr)
print("Concatenating two 2-D arrays along axis 1:")
arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

print("Stacking two 1-D arrays:")
arr = np.stack((arr1, arr2), axis=1)

print(arr)

print("Stacking two 1-D arrays using hstack:")
arr = np.hstack((arr1, arr2))

print(arr)

print("Stacking two 1-D arrays using vstack:")
arr = np.vstack((arr1, arr2))

print(arr)

print("Stacking two 1-D arrays using dstack:")
arr = np.dstack((arr1, arr2))

print(arr)

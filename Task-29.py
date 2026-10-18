import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

print("2-D array:")
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

print("3-D array:")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print('3rd element on 2nd row of 1st array: ', arr[0, 1, 2])

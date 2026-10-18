import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)
print("Convert from int to float using astype()")
arr = np.array([1.1, 2.1, 3.1])
print("Original array:")
print(arr)
newarr = arr.astype('i')
print("After conversion:")
print(newarr)
print(newarr.dtype)
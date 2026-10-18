print("Differece between coping and viewing data")
print("Copying data means making a new array and viewing data means creating a view of the original array ")
print("changes to copy will not affect original array, changes to view will affect original array and vice versa")

import numpy as np

print("original array:", np.array([1, 2, 3, 4, 5]))
print("Copying data")
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print("After copying data, changes to the original array do not affect the copy")
print(x)

print("Viewing data")
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print("After viewing data, changes to the original array affect the view")
print(x)

print("Check if the arrays own their data using the base attribute")
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print("Does x own its data? ", x.base is None)
print("Does y own its data? ", y.base is None)

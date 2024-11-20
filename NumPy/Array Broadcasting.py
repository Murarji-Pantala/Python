import numpy as np

# Create two arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Element-wise addition
result_add = array1 + array2
print("Element-wise addition:", result_add)

# Broadcasting
array3 = np.array([[1], [2], [3]])
result_broadcast = array1 + array3
print("Broadcasting result:\n", result_broadcast)

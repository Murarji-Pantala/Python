import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# Accessing elements
print("Element at (0, 1):", array_2d[0, 1])
print("First row:", array_2d[0])

# Basic operations
print("Sum of all elements:", np.sum(array_2d))
print("Mean of all elements:", np.mean(array_2d))


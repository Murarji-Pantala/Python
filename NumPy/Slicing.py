import numpy as np

# Create a 2D array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slicing
slice1 = array[:2, 1:3]
print("Slice 1:\n", slice1)

# Indexing
row_indices = [0, 1, 2]
col_indices = [0, 1, 2]
indexed_elements = array[row_indices, col_indices]
print("Indexed elements:", indexed_elements)

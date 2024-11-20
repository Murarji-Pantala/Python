import numpy as np

# Create a 1D array
array = np.arange(12)
print("Original 1D Array:", array)

# Reshape the array to 3x4
reshaped_array = array.reshape(3, 4)
print("Reshaped to 3x4:\n", reshaped_array)

# Resize the array to 2x6
resized_array = np.resize(array, (2, 6))
print("Resized to 2x6:\n", resized_array)

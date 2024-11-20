import numpy as np

# Generate random numbers
random_numbers = np.random.rand(5)
print("Random numbers:", random_numbers)

# Generate random integers
random_integers = np.random.randint(1, 10, size=5)
print("Random integers:", random_integers)

# Statistical operations
print("Mean of random numbers:", np.mean(random_numbers))
print("Standard deviation of random numbers:", np.std(random_numbers))

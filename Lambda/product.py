# lambda function

from functools import reduce

# Calculate the product of a list of numbers using a lambda function
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)

print("Product of numbers:", product)
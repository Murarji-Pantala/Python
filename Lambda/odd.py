# lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Filtered (odd) numbers:", filtered_numbers)

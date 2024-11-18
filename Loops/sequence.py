numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0

for number in numbers:
    if number % 2 == 0:
        even_sum += number

print("Sum of even numbers:", even_sum)
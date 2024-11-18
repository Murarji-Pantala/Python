#Lambda Functions

celsius = [0, 20, 40, 100]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius))

print("Temperatures in Fahrenheit:", fahrenheit)

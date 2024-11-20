l = int(input("Enter first number: "))
m = int(input("Enter second number: "))
n = int(input("Enter third number: "))

if l >= m and l >= n:
    print(f"The largest number is {l}")
elif m >= l and m >= n:
    print(f"The largest number is {m}")
else:
    print(f"The largest number is {n}")

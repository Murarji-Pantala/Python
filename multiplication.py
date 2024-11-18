# Loops for table

t = int(input("Enter the size of the multiplication table: "))

for i in range(t, t+1):
    for j in range(1, 11):
        product = i * j
        print(f"{i} x {j} = {product}", end="\n")
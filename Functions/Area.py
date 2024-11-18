#Functions

#Area of Circle or Square 

def area(shape, radius=None, side=None):
    if shape == "Circle":
        return 3.14 * (radius ** 2)
    elif shape == "Square":
        return side * side
    else:
        return "Invalid shape"

# Input shape from user
shape = input("Enter the shape (Circle or Square): ")

if shape == "Circle":
    radius = float(input("Enter radius: "))
    area_of_shape = area(shape, radius=radius)
elif shape == "Square":
    side = float(input("Enter side length: "))
    area_of_shape = area(shape, side=side)
else:
    area_of_shape = "Invalid shape"

print("Area of the shape:", area_of_shape)


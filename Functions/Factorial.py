#Functions

#Recursive Function

def factorial(n):
    # Base case
    if n == 0:
        return 1

    # Recursive case
    return n * factorial(n - 1)

# Driver Code
#if __name__ == "__main__":
n = 4

print("Factorial of", n, "is:", factorial(n))
#loops for indefinite iteration.

import random 

n=random.randint(1,100)
g=0

while g!=n:
    g=int(input("Guess a number 1 and 100"))
    if (g>n):
          print("Choose smaller number , Incorrect Guess ")
    elif (g<n):
        print("Choose Bigger number , Incorrect Guess")
    else:
          print("Correct Guess")      
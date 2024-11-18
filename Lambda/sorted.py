# lambda function

people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people = sorted(people, key=lambda x: x[1])

print("People sorted by age:", sorted_people)
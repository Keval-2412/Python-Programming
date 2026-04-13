names = ["Rahul Sharma", "Amit", "Priyanka", "Suresh Kumar", "Neha"]

result = list(filter(lambda x: len(x) > 8, names))

print("Names with length > 8:", result)
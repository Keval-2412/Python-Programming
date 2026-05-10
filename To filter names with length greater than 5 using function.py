# Python program to filter names with length greater than 5

names = list(map(str, input("Enter names separated by spaces: ").split()))

result = list(filter(lambda x: len(x) > 5, names))

print(result)
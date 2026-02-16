import random
numbers = []
i = 0
while i < 30:
    numbers.append(random.randint(-50,50))
    i += 1

print("Original list of 30 random  numbers: ")
print(numbers)

positive =[]
negative = []

i = 0
while i < len(numbers):
    if numbers[i] > 0:
        positive.append(numbers[i])
    elif numbers[i] < 0:
        negative.append(numbers[i])
    i += 1

print("\nList of Positive Numbers:")
print(positive)
print("\nList of negative numbers:")
print(negative)
import random 
numbers = []
i = 0
while i < 50:
    numbers.append(random.randint(1,30))
    i += 1

print("Original list of 50 random number: ")
print(numbers)

unique_numbers = []
i = 0
while i < len(numbers):
    if numbers[i] not in unique_numbers:
        unique_numbers.append(numbers[i])
    i +=1

print("\nList after removing duplicate values: ")
print(unique_numbers)
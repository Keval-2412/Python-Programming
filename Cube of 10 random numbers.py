# Python program to create 10 random numbers and generate cubes
import random

# Create list of 10 random numbers
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 10))

# Generate cube of each number
cubes = []
for num in numbers:
    cubes.append(num ** 3)

# Display lists
print("Original List:", numbers)
print("Cubed List:", cubes)
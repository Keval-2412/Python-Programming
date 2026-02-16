import random
numbers = []
i = 0
while i < 20:
    numbers.append(random.randint(1,50))
    i += 1
print("Generated list:")
print(numbers)

key = int(input("Enter number to search: "))

found = False
print("Positions of occurences: ")
i = 0
while i < len(numbers):
    if numbers[i] == key:
        print(i , end=" ")
        found = True
    i += 1

if not found:
    print("Number not found in the list.")
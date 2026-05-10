# Python program to find maximum using reduce()

from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

maximum = reduce(lambda x, y: x if x > y else y, numbers)

print("Maximum number =", maximum)
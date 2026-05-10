import math

# Function to return factorial list
def factorial_list(numbers):
    return list(map(math.factorial, numbers))

# Accept list input
numbers = list(map(int, input("Enter non-negative integers separated by space: ").split()))

# Display result
result = factorial_list(numbers)
print("Factorials:", result)
# Python program to find sum of list elements using function

def find_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Accept list elements from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Function call
result = find_sum(numbers)

# Display result
print("Sum of all elements:", result)
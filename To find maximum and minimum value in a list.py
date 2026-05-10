#Python program to find maximum and minimum values in a list

def find_max_min(lst):
    return max(lst), min(lst)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

maximum, minimum = find_max_min(numbers)

print("Maximum value:", maximum)
print("Minimum value:", minimum)
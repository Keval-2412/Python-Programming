#Python program to remove duplicate elements from a list

def remove_duplicates(lst):
    return list(set(lst))

numbers = list(map(int, input("Enter numbers by space between them: ").split()))

result = remove_duplicates(numbers)

print("List after removing duplicates:", result)
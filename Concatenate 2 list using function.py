# Function to concatenate lists
def concatenate_lists(list1, list2):
    return list1 + list2

# Create two lists
list1 = list(map(int, input("Enter elements of the first list (space-separated): ").split()))
list2 = list(map(int, input("Enter elements of the second list (space-separated): ").split()))

# Display result
result = concatenate_lists(list1, list2)
print("Concatenated List:", result)
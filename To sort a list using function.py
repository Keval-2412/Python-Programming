#Python program to sort a list using function

def sort_list(lst):
    lst.sort()
    return lst

numbers = list(map(int, input("Enter numbers by spaces between them: ").split()))
print(sort_list(numbers))
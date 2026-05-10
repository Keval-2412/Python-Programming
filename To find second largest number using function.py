#Python program to find second largest number

def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]

numbers = list(map(int, input("Enter numbers: ").split()))
print(second_largest(numbers))
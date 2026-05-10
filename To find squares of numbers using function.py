#Python program to calculate square of numbers in a list

def square_list(lst):
    result = []
    
    for num in lst:
        result.append(num ** 2)
        
    return result

numbers = list(map(int, input("Enter numbers by space between them: ").split()))

squares = square_list(numbers)

print("Squared list:", squares)
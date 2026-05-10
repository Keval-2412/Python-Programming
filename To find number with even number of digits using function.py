# Python program to find numbers with even number of digits
def even_digit_numbers(lst):
    result = []
    for num in lst:
        if len(str(abs(num))) % 2 == 0:   # count digits
            result.append(num)
    return result
# Accept list from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# Function call
output = even_digit_numbers(numbers)
# Display result
print("Numbers with even number of digits:", output)
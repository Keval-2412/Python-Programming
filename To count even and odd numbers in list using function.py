#Python program to count even and odd numbers in a list
def count_even_odd(lst):
    even = 0
    odd = 0
    
    for num in lst:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
            
    return even, odd
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
even_count, odd_count = count_even_odd(numbers)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
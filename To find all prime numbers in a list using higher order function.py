# Python program to find all prime numbers in a list using higher order function
def is_prime(n):
    if n < 2:
        return False
        
    for i in range(2, n):
        if n % i == 0:
            return False           
    return True

def prime_numbers(lst):
    return list(filter(is_prime, lst))

# Input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Function call
result = prime_numbers(numbers)

# Output
print("Prime numbers:", result)
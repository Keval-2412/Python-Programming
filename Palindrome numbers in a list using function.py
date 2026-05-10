# Function to find palindrome numbers
def palindrome_list(lst):
    result = []

    for num in lst:
        if str(num) == str(num)[::-1]:
            result.append(num)

    return result

# Accept list from user
a = list(map(int, input("Enter numbers separated by space: ").split()))
b = palindrome_list(a)
print("Palindrome numbers are:", b)
n = int(input("Enter a number: "))
temp = n
rev = 0
while temp > 0:
    r = temp % 10
    rev = rev * 10 + r
    temp //= 10
if rev == n:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
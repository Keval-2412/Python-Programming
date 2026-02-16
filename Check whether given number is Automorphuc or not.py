n = int(input("Enter a number: "))
square = n * n
temp = n
is_automorphic = True
while temp > 0:
    if temp % 10 != square % 10:
        is_automorphic = False
        break
    temp //= 10
    square //= 10
if is_automorphic:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
# Python program to calculate power

def power(base, exp):
    return base ** exp

b = int(input("Enter base: "))
e = int(input("Enter exponent: "))

print(power(b, e))
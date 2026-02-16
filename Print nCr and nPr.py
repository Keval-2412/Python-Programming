def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

if r > n:
    print("nCr and nPr not possible when r > n")
else:
    nCr = factorial(n) // (factorial(r) * factorial(n-r))
    nPr = factorial(n) // factorial(n-r)

    print("nCr =", nCr)
    print("nPr =", nPr)
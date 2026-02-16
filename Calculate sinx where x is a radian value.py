deg = float(input("Enter angle in degrees: "))
n = int(input("Enter number of terms: "))

x = deg * 3.14159/180

sinx = 0
sign = 1

for i in range(1,2*n,2):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sinx = sinx + sign * (x ** i) /fact
    sign = sign * (-1)

print("sin(", deg, ") = ", sinx) 
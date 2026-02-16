n =int(input("Enter a number:"))

if n > 1:
    i = 2
    is_Prime = True
    while i <= n //2:
     if n % i == 0:
        is_Prime = False
        break
     i += 1
    if is_Prime:
        print("Prime Number.")
    else:
        print("Not a Prime Number.")
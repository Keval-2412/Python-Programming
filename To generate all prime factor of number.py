def prime_factors(n):
    print("Prime factors are:", end=" ")
    i = 2
    while i <= n:
        if n % i == 0:
            print(i, end=" ")
            while n % i == 0:   # remove all occurrences
                n = n // i
        i += 1
num = int(input("Enter a number: "))
prime_factors(num)
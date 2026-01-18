a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

if a >= b and a >= c:
    largest = a
elif b >= a:
    largest = b
else:
    largest = c

if a <= b and a <= c:
        smallest = a
elif b <= a:
        smallest = b
else:
        smallest = c
        print("LARGEST NUMBER: ", largest)
        print("SMALLEST NUMBER: ", smallest)
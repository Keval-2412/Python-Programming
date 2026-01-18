length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

if area > perimeter:
    print("Area is greater than perimeter.")
else:
    print("Area is NOT greater than perimeter.")

print("Area:", area)
print("Perimeter:", perimeter)

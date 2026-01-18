x = float(input("Enter x-coordinate of center: "))
y = float(input("Enter y-coordinate of center: "))
r = float(input("Enter radius of circle: "))

x1 = float(input("Enter x-coordinate of point: "))
y1 = float(input("Enter y-coordinate of point: "))

distance = math.sqrt(pow(x1 - x, 2) + pow(y1 - y, 2))

if distance < r:
    print("Point lies INSIDE the circle.")
elif distance == r:
    print("Point lies ON the circle.")
else:
    print("Point lies OUTSIDE the circle.")
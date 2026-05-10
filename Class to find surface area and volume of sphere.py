import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3


r = float(input("Enter radius: "))
s = Sphere(r)

print("Surface Area:", s.surface_area())
print("Volume:", s.volume())
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def calculate_area(radius):
        return math.pi * (radius ** 2)

    @classmethod
    def calculate_perimeter(cls, radius):
            return 2 * math.pi * radius

radius = int(input("radius: "))
circle = Circle(radius)

area = Circle.calculate_area(radius)
print(f"При радиус{radius} е: {area:.2f}")

perimeter = Circle.calculate_perimeter(radius)
print(f"При радиус {radius} е: {perimeter:.2f}")

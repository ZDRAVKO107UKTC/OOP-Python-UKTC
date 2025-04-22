import math
class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        
    def calculate_area(self):
        p = (self.A + self.B + self.C) / 2
        s = math.sqrt(s * (s - self.A) * (s - self.B) * (s - self.C))
        return  s
    
    def sides(self):
        return self.A, self.B, self.C
    
    def perimeter(self):
        return self.A + self.B + self.C
    
    @staticmethod
    def input_shape():
        shape = input("Enter the shape (triangle, rectangle, square): ")
        if shape.lower() == "triangle":
            A = float(input("Enter side A: "))
            B = float(input("Enter side B: "))
            C = float(input("Enter side C: "))
            return Triangle(A, B, C)
        else:
            print("Invalid shape entered.")
            return None

Triangles = []

num_triangles = int(input("How many triangles would you like to create? "))

for i in range(num_triangles):
    new_triangle = Triangle.input_shape()
    if new_triangle:
        Triangles.append(new_triangle)

for i, triangle in enumerate(Triangles, start=1):
    print(f"\nTriangle {i}:")
    print(f"Sides: {triangle.sides()}")
    print(f"Perimeter: {triangle.perimeter()}")
    print(f"Area: {triangle.calculate_area():.2f}")

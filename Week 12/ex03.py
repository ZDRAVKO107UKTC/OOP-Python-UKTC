class Shape:
    def площ(self):
        pass

class Успоредник(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def площ(self):
        return self.base * self.height

class Трапец(Shape):
    def __init__(self, a, b, height):
        self.a = a
        self.b = b
        self.height = height

    def площ(self):
        return (self.a + self.b) * self.height / 2

успоредник = Успоредник(5, 10)
трапец = Трапец(3, 7, 4)

фигури = [успоредник, трапец]

for фигура in фигури:
    print(f"Площта на фигурата е: {фигура.площ()}")
class Building:
    def __init__(self, height, area, address):
        self.height = height
        self.area = area
        self.address = address

    def display(self):
        print(f"Building at {self.address}:")
        print(f"  Height: {self.height} meters")
        print(f"  Area: {self.area:.2f} square meters")


class House(Building):
    def __init__(self, height, area, address, floors, owner):
        super().__init__(height, area, address)
        self.floors = floors
        self.owner = owner

    def display(self):
        super().display()
        print(f"  Floors: {self.floors}")
        print(f"  Owner: {self.owner}")

    def average_floor_height(self):
        if self.floors == 0:
            return 0
        return self.height / self.floors


def find_most_spacious_house(houses):
    if not houses:
        return None
    return max(houses, key=lambda house: house.average_floor_height())



house1 = House(10, 150.5, "123 Main St", 2, "John Doe")
house2 = House(15, 200.0, "456 Elm St", 3, "Jane Smith")
house3 = House(8, 120.0, "789 Oak St", 1, "Alice Brown")

houses = [house1, house2, house3]

for house in houses:
    house.display()
    print()

most_spacious_house = find_most_spacious_house(houses)
if most_spacious_house:
    print("The most spacious house is:")
    most_spacious_house.display()

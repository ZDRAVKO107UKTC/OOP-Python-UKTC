class Car:
    wheels = 4

    def __init__(self, car_brand, car_model, car_color, car_price, manufacture_year):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_color = car_color
        self.car_price = car_price
        self.manufacture_year = manufacture_year

    def display_info(self):
        print("Car Brand:", self.car_brand)
        print("Car Model:", self.car_model)
        print("Car Color:", self.car_color)
        print("Car Price:", self.car_price)
        print("Manufacture Year:", self.manufacture_year)
        print("-------------------------")
        print("\n")


    @classmethod
    def change_wheels(cls):
        cls.wheels = 6
        print("Wheels changed to", cls.wheels)

def sort_price(cars):
    return sorted(cars, key=lambda car: car.car_price)

def list_by_brand(cars, brand):
    return [car for car in cars if car.car_brand.lower() == brand.lower()]

def search_color(cars, color):
    return [car for car in cars if car.car_color.lower() == color.lower()]

def newest_car(cars):
    return max(cars, key=lambda car: car.manufacture_year)

# Main program
num_cars = int(input("Number of cars: "))
cars = []
for _ in range(num_cars):
    car_brand = input("Enter car brand: ")
    car_model = input("Enter car model: ")
    car_color = input("Enter car color: ")
    car_price = float(input("Enter car price: "))
    manufacture_year = int(input("Enter manufacture year: "))

    car = Car(car_brand, car_model, car_color, car_price, manufacture_year)
    cars.append(car)

# Example usage of the functions
sorted_cars = sort_price(cars)
print("\nCars sorted by price:")
for car in sorted_cars:
    car.display_info()

brand_to_search = input("\nEnter brand to list cars: ")
cars_by_brand = list_by_brand(cars, brand_to_search)
print(f"\nCars of brand '{brand_to_search}':")
for car in cars_by_brand:
    car.display_info()

color_to_search = input("\nEnter color to search cars: ")
cars_by_color = search_color(cars, color_to_search)
print(f"\nCars of color '{color_to_search}':")
for car in cars_by_color:
    car.display_info()


newest = newest_car(cars)
print("\nNewest car:")
newest.display_info()
class Phone():
    def __init__(self, brand, model, price, color, manufacture_year):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.manufacture_year = manufacture_year
            
    def discaunt(self):
        if 2015 <= self.manufacture_year < 2021:
            return self.price * 0.05
        elif self.manufacture_year < 2015:
            return self.price * 0.15
        elif self.manufacture_year > 2021:
            return self.price
        else:
            return "NO"
    
    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price} EUR, Color: {self.color}, Manufacture Year: {self.manufacture_year}"
        

phone1 = Phone("Apple", "iPhone 13 Pro", 1200, "Space Gray", 2021)
phone2 = Phone("Samsung", "Galaxy S21 Ultra", 1000, "Blue", 2020)
phone3 = Phone("Xiaomi", "Mi 11", 800, "Black", 2020)


print(phone1.get_info())
print("Discount:", phone1.discaunt())

print(phone2.get_info())
print("Discount:", phone2.discaunt())

print(phone3.get_info())
print("Discount:", phone3.discaunt())

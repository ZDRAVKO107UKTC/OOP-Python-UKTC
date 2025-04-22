class TV:
    def __init__(self, brand, price, model, color, manufacture_year):
        self.brand = brand
        self.price = price
        self.model = model
        self.color = color
        self.manufacture_year = manufacture_year
    
    def get_discounted_price(self):
        if 2015 <= self.manufacture_year <= 2020:
            return self.price * 0.5
        elif self.manufacture_year < 2015:
            return self.price * 0.15
        elif self.manufacture_year > 2021:
            return self.price
        
    def delete_tv(self, model, color, tv_list):
        for tv in tv_list:
            if tv.model == model and tv.color == color:
                tv_list.remove(tv)
                print("TV deleted successfully.")
                print(tv_list)
                return
   
    
    def expensive(self, price, manufacture_year, tv_list):
        for tv in tv_list:
            if tv.price > price and tv.manufacture_year >= manufacture_year:
                return tv.model, tv.color
        print("No matching TV found.")
        return None, None
        
    def sort_tv(self, model, color, tv_list):
        sorted_list = sorted(tv_list, key=lambda x: (x.model, x.color))
        for tv in sorted_list:
            if tv.model == model and tv.color == color:
                return tv.price
        print("No matching TV found.")
        return None
    
    def search_tv(self, model, color, tv_list):
        for tv in tv_list:
            if tv.model == model and tv.color == color:
                return f"Brand: {tv.brand}, Price: {tv.price} EUR"
        print("No matching TV found.")
        return None
    

tv1 = TV("Samsung", 2000, "UE43MU6500", "Black", 2018)
tv2 = TV("Sony", 1500, "KD-55X9505", "White", 2019)
tv3 = TV("LG", 1800, "OLED65Q8", "Blue", 2020)

tv_list = [tv1, tv2, tv3]

print(tv1.get_discounted_price())
print(tv2.get_discounted_price())
print(tv3.get_discounted_price())

tv1.delete_tv("UE43MU6500", "Black", tv_list)
tv2.delete_tv("KD-55X9505", "White", tv_list)
tv3.delete_tv("OLED65Q8", "Blue", tv_list)

print(tv1.expensive(1800, 2019, tv_list))
print(tv2.expensive(1500, 2018, tv_list))
print(tv3.expensive(1800, 2020, tv_list))

print(tv1.sort_tv("Sony", "White", tv_list))
print(tv2.sort_tv("Samsung", "Black", tv_list))
print(tv3.sort_tv("LG", "Blue", tv_list))

print(tv1.search_tv("Sony", "White", tv_list))
print(tv2.search_tv("Samsung", "Black", tv_list))
print(tv3.search_tv("LG", "Blue", tv_list))
print(tv1.search_tv("Sony", "Black", tv_list))
print(tv2.search_tv("Samsung", "White", tv_list))
print(tv3.search_tv("LG", "Red", tv_list))

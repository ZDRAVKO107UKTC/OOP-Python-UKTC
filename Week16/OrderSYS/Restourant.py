from Pizza import Pizza
from Salad import Salad

class Restaurant:
    def __init__(self, restaurant_name, cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine
        self.number_served = 0
        self.number_served_in_order = 0

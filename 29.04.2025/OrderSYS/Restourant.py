from Pizza import Pizza
from Salad import Salad
from OrderIter import OrderIterator

class Restaurant:
    def __init__(self, restaurant_name, cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine
        self.orders = []

    def add_order(self, item):
        self.orders.append(item)

    def serve_orders(self):
        for order in OrderIterator(self.orders):
            order.prepare()

r = Restaurant("V-zone Bar & Dinner", "Международна кухня")

r.add_order(Pizza("Пеперони", 9.9))
r.add_order(Salad("Цезар", 6.5))
r.add_order(Pizza("Четири сирена", 10.5))
r.add_order(Salad("Капрезе", 5.8))

r.serve_orders()
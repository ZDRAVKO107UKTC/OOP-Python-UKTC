from DeliveryItem import DeliveryItem
from Track import track_delivery

class Package(DeliveryItem):
    @track_delivery
    def car_delivery(self):
        print(f"Package with order #{self._order_num} is loaded into a van.")

    @track_delivery
    def delivery(self):
        print(f"Delivering package to: {self._name}, size: {self._size}, price: {self._price} BGN.")

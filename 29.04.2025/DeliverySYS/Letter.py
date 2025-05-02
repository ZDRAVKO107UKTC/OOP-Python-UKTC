from DeliveryItem import DeliveryItem
from Track import track_delivery

class Letter(DeliveryItem):
    @track_delivery
    def car_delivery(self):
        print(f"Letter with order #{self._order_num} is loaded into a small car.")

    @track_delivery
    def delivery(self):
        print(f"Delivering letter to: {self._name}, size: {self._size}, price: {self._price} BGN.")

from abc import ABC, abstractmethod

class DeliveryItem(ABC):
    def __init__(self, name, order_num, size, price):
        self._name = name
        self._order_num = order_num
        self._size = size
        self._price = price

    @abstractmethod
    def car_delivery(self):
        pass

    @abstractmethod
    def delivery(self):
        pass
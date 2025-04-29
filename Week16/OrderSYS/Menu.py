from abc import ABC, abstractmethod

class MenuItem(ABC):
    @abstractmethod
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price(self):
        return self.price

    @abstractmethod
    def prepare(self):
        pass
from Menu import MenuItem
from Log import log_action
class Pizza(MenuItem):
    def __init__(self, name="Маргарита", price=8.5):
        super().__init__(name, price)
    @log_action
    def prepare(self):
        print(f"Приготвяне на пица {self.name}...")

    def price(self):
        return self._price

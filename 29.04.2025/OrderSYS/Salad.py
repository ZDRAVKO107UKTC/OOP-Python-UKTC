from Menu import MenuItem
from Log import log_action
class Salad(MenuItem):
    def __init__(self, name="Гръцка салата", price=5.0):
        super().__init__(name, price)
    @log_action
    def prepare(self):
        print(f"Приготвяне на салата {self.name}...")

    def price(self):
        return self._price

from PaymentMethod import PaymentMethod
from Authorise import authorize

class PayPal(PaymentMethod):
    def __init__(self, holder, CVV, Exp_DATE, Card_Number):
        super().__init__(holder, CVV, Exp_DATE, Card_Number)
    @authorize
    def pay(self):
        print(f"PayPal Payment: Holder {self.holder}, Email/ID {self.Card_Number}")

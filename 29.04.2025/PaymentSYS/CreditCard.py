from PaymentMethod import PaymentMethod
from Authorise import authorize

class CreditCard(PaymentMethod):
    def __init__(self, holder, CVV, Exp_DATE, Card_Number):
        super().__init__(holder, CVV, Exp_DATE, Card_Number)
    @authorize
    def pay(self):
        print(f"CreditCard Payment: Holder {self.holder}, Card {self.Card_Number}")

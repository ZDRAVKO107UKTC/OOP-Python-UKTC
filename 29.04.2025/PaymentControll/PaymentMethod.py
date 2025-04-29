from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    def __init__(self, holder, CVV, Exp_DATE, Card_Number ):
        self.holder = holder
        self.CVV = CVV
        self.Exp_DATE = Exp_DATE
        self.Card_Number = Card_Number

    @abstractmethod
    def pay(self):
        pass
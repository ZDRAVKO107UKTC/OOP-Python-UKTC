from Iterator import Iterator
from CreditCard import CreditCard
from PayPal import PayPal

cc = CreditCard("Ivan Petrov", "123", "12/26", "4111111111111111")
pp = PayPal("Maria Ivanova", "321", "11/25", "maria@example.com")

transactions = [cc, pp]

transaction_iterator = Iterator(transactions)

for transaction in transaction_iterator:
    transaction.pay()

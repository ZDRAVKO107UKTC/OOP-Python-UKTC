from Letter import Letter
from Package import Package
from Iterator import DeliveryIterator
from Generator import filter_expensive_deliveries

deliveries = [
    Letter("Ivan Petrov", 101, "A4", 2.5),
    Package("Maria Ivanova", 102, "Box", 12.0),
    Letter("Georgi Georgiev", 103, "A5", 1.8),
    Package("Anna Dimitrova", 104, "Large Box", 18.3)
]


print("=== All deliveries ===")
for d in DeliveryIterator(deliveries):
    d.car_delivery()
    d.delivery()

print("\n=== Expensive deliveries (>5.0 BGN) ===")
for d in filter_expensive_deliveries(deliveries):
    d.delivery()

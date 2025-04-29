class Delivery:
    def __init__(self, address, status):
        self.address = address
        self.__status = status

    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        self.__status = new_status


class DeliveryLog:
    def __init__(self, deliveries):
        self.deliveries = deliveries
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.deliveries):
            raise StopIteration
        delivery = self.deliveries[self.index]
        self.index += 1
        return delivery


def deliveries_log(delivery_log):
    for delivery in delivery_log:

        if delivery.get_status().lower() == "delivered":
            print(f"THE DELIVERY TO {delivery.address} IS COMPLETED")

        if delivery.get_status().lower() == "pending":
            print(f"THE DELIVERY TO {delivery.address} IS PENDING")


deliveries = [
    Delivery("ул. Витоша 10", "Pending"),
    Delivery("бул. България 5", "Delivered"),
    Delivery("ул. Симеон 3", "deLivered"),
    Delivery("ул.Перуша", "pending")
]

log = DeliveryLog(deliveries)
deliveries_log(log)

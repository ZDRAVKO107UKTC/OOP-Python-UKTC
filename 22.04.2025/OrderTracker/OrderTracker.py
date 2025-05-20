class OrderTracker:
    def __init__(self, orders):
        self.orders = orders
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.orders):
            order = self.orders[self.index]
            self.index += 1
            return order
        else:
            raise StopIteration


def notify_shipped(order_iterator):
    for order in order_iterator:
        if order.get("status").lower() == "shipped":
            yield f"Поръчка #{order.get('id')} е изпратена."


orders = [
    {"id": 101, "status": "processing"},
    {"id": 102, "status": "shipped"},
    {"id": 103, "status": "shipped"}
]

tracker = OrderTracker(orders)
for message in notify_shipped(tracker):
    print(message)

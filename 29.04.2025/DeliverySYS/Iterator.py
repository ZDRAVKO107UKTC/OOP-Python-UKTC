class DeliveryIterator:
    def __init__(self, deliveries):
        self._deliveries = deliveries
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._deliveries):
            item = self._deliveries[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

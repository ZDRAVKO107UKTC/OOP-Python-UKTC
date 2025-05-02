def filter_expensive_deliveries(deliveries, threshold=5.0):
    for item in deliveries:
        if item._price > threshold:
            yield item

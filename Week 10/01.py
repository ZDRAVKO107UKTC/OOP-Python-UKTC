class Market:
    def __init__(self, barcod, name, price, quantity):
        self.barcod = barcod
        self.name = name
        self.price = price
        self.quantity = quantity

    def sale(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            return True
        else:
            return False

    def discount(self):
        if 30 <= self.price <= 50:
            self.price *= 0.97
        elif 10 <= self.price < 30:
            self.price *= 0.93

def search_by_barcod(product_list, barcod):
    for product in product_list:
        if product.barcod == barcod:
            print(f'Product found: {product.name}, Price: {product.price}, Quantity: {product.quantity}')
            return
    print("NO barcode !!!")
    print("Available barcodes:", [product.barcod for product in product_list])

def sort_by_quantity(product_list):
    sorted_list = sorted(product_list, key=lambda x: x.quantity)
    for product in sorted_list:
        print(f'Product: {product.name}, Quantity: {product.quantity}')

n = int(input("Enter number of products: "))
product_list = []

for _ in range(n):
    barcod = input("Enter barcode: ")
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    product_list.append(Market(barcod, name, price, quantity))

search_barcod = input("Enter barcode to search: ")
search_by_barcod(product_list, search_barcod)

sort_by_quantity(product_list)
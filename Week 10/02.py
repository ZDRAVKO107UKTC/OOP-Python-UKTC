class Product:
    def __init__(self, name, code, weight, dimensions):
        self.name = name
        self.code = code
        self.weight = weight
        self.dimensions = dimensions

    @staticmethod
    def display_info(product):
        print(f'Product Name: {product.name}, Code: {product.code}, Weight: {product.weight}kg, Dimensions: {product.dimensions}cm')

    @classmethod
    def create_product(cls):
        name = input("Enter product name (max 20 characters): ")[:20]
        code = input("Enter product code (max 10 digits): ")[:10]
        weight = float(input("Enter weight in kg: "))
        dimensions = tuple(map(int, input("Enter dimensions (length, width, height) in cm separated by space: ").split()))
        return cls(name, code, weight, dimensions)

products = []
for _ in range(3):
    products.append(Product.create_product())

for product in products:
    Product.display_info(product)
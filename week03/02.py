class aritmetica:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero is not allowed."

num1 = int(input())
num2 = int(input())

num = aritmetica(num1, num2)


print("Addition:", num.add())
print("Subtraction:", num.subtract())
print("Multiplication:", num.multiply())
print("Division:", num.divide())

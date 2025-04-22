from math import factorial as f

class Number():
    def __init__(self, num):
        self.num = num

    def calculate_factorial(self):
        return f(self.num)
    
    def up_num(self):
        return self.num ** 2
    
    def up_num2(self):
        return self.num ** 3
    
number = Number(int(input()))

print("Factorial:", number.calculate_factorial())
print("2:", number.up_num())
print("3:", number.up_num2())

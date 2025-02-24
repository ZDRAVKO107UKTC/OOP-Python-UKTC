class Number:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Number' and '{}'".format(type(other).__name__))

num1 = Number(5)
num2 = Number(10)
result = num1 * num2
print(result.value)
class Number:
    def __init__(self, value):
        self.value = value

    def print_num(self):
        return f"NUM:{self.value}"


class Doublenum(Number):
    def __init__(self, value, num2 ):
        super().__init__(value)
        self.num2 = num2

    def print_num2(self):
        return f"NUM2:{self.value} {self.num2}"

value = Number(5)
num2 = Doublenum(7, 6)

print(value.print_num())
print(num2.print_num2())
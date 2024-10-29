import math as mat

class number:
    def __init__(self, number):
        self.number = number
        
a = int(input("Enter number: "))
N = number(a)

print("Your number is :", N.number)

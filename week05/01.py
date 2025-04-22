from libxml2mod import parent


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_parent(self):
        return f"Parent: {self.name, self.age}"

class Child(Parent):
    def __init__(self, name, age, town):
        super().__init__(name, age)
        self.town = town


    def print_child(self):
        return f"Child: {self.name}, {self.town}"


father = Parent("Zdravko", 25)
child = Child("Ivan", 25, "Pernik")

print(father.print_parent())
print(child.print_child())


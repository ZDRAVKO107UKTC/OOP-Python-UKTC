class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def get_inf(self):
        return f"Name: {self.name}, family: {self.family}, Age: {self.age}, Nationality: {self.nationality}"

person01 = Person("Ivan", "Ivanov", 30, "Bulgarian")
person02 = Person("Mariq", "Petrova", 25, "GErman")

print(person01.get_inf())
print(person02.get_inf())

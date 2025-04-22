class Person:
    def __init__(self, name, age, family, nationality):
        self.name = name
        self.age = age
        self.family = family
        self.nationality = nationality
    
    def input_data(self):
        self.name = input("Name: ")
        self.age = int(input("Age: "))
        self.family = input("Family: ")
        self.nationality = input("Nationality: ")
        
    def print(self):
        print(f"Name: {self.name}, Age: {self.age}, Family: {self.family}, Nationality: {self.nationality}")
        
persons = []
new_persons = input("New persons: ")

for i in range(int(new_persons)):
    person = Person("", 0, "", "")
    person.input_data()
    persons.append(person)
    

for person in persons:
    person.print()
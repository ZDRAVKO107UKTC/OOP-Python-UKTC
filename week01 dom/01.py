class Person:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

Name = input()
Age = int(input())
Grade = float(input())

person= Person(Name, Age, Grade)


print(person.name)
print(person.age)
print(person.grade)

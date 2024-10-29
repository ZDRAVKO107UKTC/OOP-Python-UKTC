class Person:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
name = input("NAME:")
age = int(input("AGE:"))
grade = float(input("GRADE:"))

person = Person(name, age, grade)

print("Name:", person.name)
print("Age:", person.age)
print("Grade:", person.grade)
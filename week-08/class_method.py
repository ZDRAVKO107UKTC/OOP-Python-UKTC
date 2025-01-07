class Student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, name):
        print(Student.school_name)
        Student.school_name = name

jessa = Student("Jessa", 14)
Student.change_school("XYZ School")
print(jessa.school_name)

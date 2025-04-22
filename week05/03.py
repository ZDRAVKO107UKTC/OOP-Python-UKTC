class Student:
    def __init__(self, name, age, school_name):
        self.name = name
        self.age = age
        self.school_name = school_name

    def display_info(self):
        print(f"Име: {self.name}, Възраст: {self.age}, Училище: {self.school_name}")


class Group(Student):
    def __init__(self, name, age, school_name, group_number, student_number):
        super().__init__(name, age, school_name)
        self.group_number = group_number
        self.student_number = student_number

    def display_full_info(self):
        print(f"Име: {self.name}, Възраст: {self.age}, Училище: {self.school_name}, "
              f"Номер на група: {self.group_number}, Номер на ученик: {self.student_number}")


def main():
    students = []
    num_students = int(input("Въведете брой ученици: "))

    for i in range(num_students):
        name = input(f"Въведете име на ученик {i + 1}: ")
        age = int(input(f"Въведете възраст на ученик {i + 1}: "))
        school_name = input(f"Въведете име на училище за ученик {i + 1}: ")
        group_number = int(input(f"Въведете номер на групата за ученик {i + 1}: "))
        student_number = int(input(f"Въведете номер на ученика в групата {i + 1}: "))
        students.append(Group(name, age, school_name, group_number, student_number))

    print("\nОсновни данни за всички ученици:")
    for student in students:
        print(f"Име: {student.name}, Възраст: {student.age}")

    selected_group = int(input("\nВъведете номер на група, за да покажете учениците от тази група: "))
    print(f"\nДанни за учениците в група {selected_group}:")
    for student in students:
        if student.group_number == selected_group:
            student.display_full_info()


if __name__ == "__main__":
    main()

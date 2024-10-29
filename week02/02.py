class Firma:
    def __init__(self, id_num, fname, iname, experience_firma, salary, age):
        self.id_num = id_num
        self.fname = fname
        self.iname = iname
        self.experience_firma = experience_firma
        self.salary = salary
        self.age = age
    
    def calculate_salary(self):
        if self.experience_firma < 5:
            return self.salary * 0.5
        elif self.experience_firma <= 10:
            return self.salary * 1.5
        else:
            return self.salary * 2

def input_employee_data(num):
    id_num = int(input(f"Enter employee {num} ID: "))
    fname = input(f"Enter employee {num} first name: ")
    iname = input(f"Enter employee {num} last name: ")
    experience_firma = int(input(f"Enter employee {num} experience in years: "))
    salary = int(input(f"Enter employee {num} salary: "))
    age = int(input(f"Enter employee {num} age: "))
    return Firma(id_num, fname, iname, experience_firma, salary, age)

employee_list = []

num_employees = int(input("Enter number of employees: "))

for i in range(1, num_employees + 1):
    employee = input_employee_data(i)
    employee_list.append(employee)

for i, employee in enumerate(employee_list, 1):
    print(f"Employee {i} calculated salary: {employee.calculate_salary()}")


import random


employees = []


class Employee:
    def __init__(self, number, name, age, email):
        self.number = number
        self.name = name
        self.age = age
        self.email = email

    def get_employee_info(self):
        print(
            f"""
            Employee Number: {self.number}
            Name: {self.name}
            Age: {self.age}
            Email: {self.email}
            """
        )


ryan = Employee(1, "Ryan", 22, "ryan@company.com")


def add_new_employee():
    number = random.randint(0, 10000)
    name = input("Employee name: \n")
    age = input("Employee age: \n")
    email = input("Employee email: \n")

    new_employee = Employee(number, name, age, email)
    return new_employee


new_employee_ = add_new_employee()
employees.append(new_employee_)
print(employees)

employees[0].get_employee_info()

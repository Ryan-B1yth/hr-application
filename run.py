import random


employees = []


class Employee:
    """
        Creates an instance of an Employee.
    """
    def __init__(self, number, name, age, email):
        self.number = number
        self.name = name
        self.age = age
        self.email = email

    """
        Prints employee info in terminal.
    """
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
    employees.append(new_employee)
    print(new_employee.get_employee_info())


def get_employee(number):
    for employee in employees:
        if employee.number == number:
            print(employee.get_employee_info())


while True:
    print("""
    Add new employee (A), check employee details (C),
    or exit (E)?
    """)
    answer = input("\n").lower()
    if answer == "a":
        add_new_employee()
        continue
    elif answer == "c":
        num_to_check = int(input("Enter employee number: \n"))
        get_employee(num_to_check)
    elif answer == "e":
        exit()
    else:
        print("Invalid input, please try again. Input A/C only.")
        continue

print(employees)
print(employees[0].get_employee_info())

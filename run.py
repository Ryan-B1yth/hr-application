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


def user_action():
    print("Add new employee or check employee details?")
    action = input("\n")
    return action
    

def add_new_employee():
    number = random.randint(0, 10000)
    name = input("Employee name: \n")
    age = input("Employee age: \n")
    email = input("Employee email: \n")

    new_employee = Employee(number, name, age, email)
    employees.append(new_employee)


while True:
    print("Add new employee (A) or check employee details (C)?")
    answer = input("\n").lower()
    if answer == "a":
        add_new_employee()
        break
    elif answer == "c":
        pass
    else:
        print("Invalid input, please try again. Input A/C only.")
        continue

print(employees)
print(employees[0].get_employee_info())

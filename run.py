import random
import datetime

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
        Gets the current date and time.
    """
    def get_datetime():
        date_time = datetime.datetime.now()
        date_time_now = date_time.strftime("%x")
        return date_time_now
   
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
            Date added: {Employee.get_datetime()}
            """
        )


def add_new_employee():
    # Gives the employee details
    number = random.randint(1000, 9999)
    name = input("Employee name: \n")
    age = input("Employee age: \n")
    email = input("Employee email: \n")

    # Adds employee to list
    new_employee = Employee(number, name, age, email)
    employees.append(new_employee)
    print(new_employee.get_employee_info())


def get_employee(number):
    # Finds the employee
    for employee in employees:
        if employee.number == number:
            print(employee.get_employee_info())
    
    delete = input("Back to search (B) or delete (DEL)? \n").lower()
    if delete == "del":
        remove_employee(number)


def remove_employee(number):
    for employee in employees:
        if employee.number == number:
            employees.remove(employee)


def list_employees():
    for employee in employees:
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
    elif answer == "all":
        list_employees()
    else:
        print("Invalid input, please try again. Input A/C/E only.")
        continue

import random
import datetime
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hr_application')

EMPLOYEES = SHEET.worksheet("hr_list")


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
        return (
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
    employee_object = Employee(number, name, age, email)
    new_employee = [number, name, age, email, Employee.get_datetime()]
    EMPLOYEES.append_row(new_employee)
    print(employee_object.get_employee_info())


def get_employee(number):
    employee = EMPLOYEES.find(str(number))
    row = EMPLOYEES.row_values(employee.row)
    employee_object = Employee(row[0], row[1], row[2], row[3])
    print(employee_object.get_employee_info())

    delete = input("Back to search (ANY KEY) or delete (DEL)? \n").lower()
    if delete == "del":
        EMPLOYEES.delete_rows(employee.row)



def remove_employee(number):
    for employee in SHEET:
        if employee.number == number:
            EMPLOYEES.delete_rows(employee)


def list_employees():
    employees_list = EMPLOYEES.get_all_values()
    for employee in employees_list:
        employee_object = Employee(employee[0], employee[1],
        employee[2], employee[3])
        print(employee_object.get_employee_info())


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
        try:
            num_to_check = int(input("Enter employee number: \n"))
            get_employee(num_to_check)
        except AttributeError:
            print("Number not assigned.")
        except ValueError:
            print("Invalid input. Number only please.")

    elif answer == "e":
        exit()
    elif answer == "all":
        list_employees()
    else:
        print("Invalid input, please try again. Input A/C/E only.")
        continue

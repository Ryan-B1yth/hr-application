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
    employee_object = Employee(number, name, age, email)
    new_employee = [number, name, age, email, Employee.get_datetime()]
    EMPLOYEES.append_row(new_employee)
    print(employee_object.get_employee_info())


def get_employee(number):
    employee = EMPLOYEES.find(str(number))
    row = EMPLOYEES.row_values(employee.row)
    print(
        f"""
        Number: {row[0]}
        Name: {row[1]}
        Age: {row[2]}
        Email: {row[3]}
        Date added: {row[4]}
        """
    )

    delete = input("Back to search (ANY KEY) or delete (DEL)? \n").lower()
    if delete == "del":
        EMPLOYEES.delete_rows(employee.row)



def remove_employee(number):
    for employee in SHEET:
        if employee.number == number:
            EMPLOYEES.delete_rows(employee)


def list_employees():
    employess_list = EMPLOYEES.get_all_values()
    for employee in employess_list:
        print(f"""
        Number: {employee[0]}
        Name: {employee[1]}
        Age: {employee[2]}
        Email: {employee[3]}
        Date added: {employee[4]}
        """)


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

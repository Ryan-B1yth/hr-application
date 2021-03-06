"""
    Imports necessary libraries.
"""
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
    def __init__(self, number, name, age, email, salary):
        self.number = number
        self.name = name
        self.age = age
        self.email = email
        self.salary = salary

    def get_employee_info(self):
        """
        Prints employee info in terminal.
        """
        return (
            f"""
        --------------------------------------
            Employee Number: {self.number}
            Name: {self.name}
            Age: {self.age}
            Email: {self.email}
            Salary: £{self.salary}
            Date added: {get_datetime()}
        --------------------------------------
            """
        )

    def get_basic_info(self):
        """
        Only show basic info during an all employees search.
        """

        return (
            f"""
        --------------------------------------
            Employee Number: {self.number}
            Name: {self.name}
        --------------------------------------
            """
        )


def add_new_employee():
    """
    Adds a new employee to the google sheet.
    """
    # Gives the employee details
    number = random.randint(1000, 9999)

    name = input("Employee name: \n")

    while True:
        try:
            age = int(input("Employee age: \n"))
            break
        except ValueError:
            print("Please enter a number.")

    email = input("Employee email: \n")

    salary = get_salary()

    # Adds employee to list
    print("Adding employee...")
    employee_object = Employee(number, name, age, email, salary)
    new_employee = [number, name, age, email, salary, get_datetime()]
    EMPLOYEES.append_row(new_employee)
    print("Employee added successfully.")
    print(employee_object.get_employee_info())


def get_salary():
    """
    Sets employee salary based on input.
    """
    salary_input = input("""
        Basic (B)
        Manager (M)
        C Suite (C)
        Manual input (ANY KEY)\n""").lower()

    if salary_input == "b":
        salary = "20,000"
    elif salary_input == "m":
        salary = "30,000"
    elif salary_input == "c":
        salary = "50,000"
    else:
        salary = input("Manual input: \n")

    return salary


def get_datetime():
    """
    Gets the current date and time.
    """
    date_time = datetime.datetime.now()
    date_time_now = date_time.strftime("%x")
    return date_time_now


def get_employee(number):
    """
    Finds employee information and displys in terminal.
    """
    employee = EMPLOYEES.find(str(number))
    row = EMPLOYEES.row_values(employee.row)
    employee_object = Employee(row[0], row[1], row[2], row[3], row[4])
    print(employee_object.get_employee_info())

    # Actions the user can take after retrieving employee info.
    action = input("""
        Back to search (ANY KEY)
        Delete (DEL)
        Change details (C) \n
        """).lower()
    if action == "del":
        print("Deleting employee...")
        EMPLOYEES.delete_rows(employee.row)
        print("Employee deleted successfully.")
    elif action == "c":
        change = input("""Change employee:
        Name (N)
        Age (A)
        Email (E)
        Salary (S)\n
        """).lower()
        if change == "n":
            item = 2
        elif change == "a":
            item = 3
        elif change == "e":
            item = 4
        elif change == "s":
            item = 5
        else:
            print("Invalid input, returning to main menu.")
            return
        change_to = input("Please enter the change:\n")
        print("Updating employee information...")
        EMPLOYEES.update_cell(int(employee.row), item, change_to)
        print("Employee information updated successfully.")


def list_employees():
    """
    Lists all employees on google sheet using basic info function
    in Employee class.
    """
    employees_list = EMPLOYEES.get_all_values()
    for employee in employees_list[1:]:
        employee_object = Employee(
            employee[0], employee[1],
            employee[2], employee[3], employee[4])
        print(employee_object.get_basic_info())


def main():
    """
    Executes the main program.
    """
    print("""Welcome to Company and Co's HR program.
    Please select from the options below""")
    while True:
        print("""
        Add new employee: (A)
        Check employee details: (C)
        List all employees: (ALL)
        Exit (E)
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
            print("Exiting program. Have a nice day!")
            exit()
        elif answer == "all":
            list_employees()
        else:
            print("Invalid input, please try again.")
            continue


main()

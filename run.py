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

ryan.get_employee_info()
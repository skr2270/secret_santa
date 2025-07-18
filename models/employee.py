# models/employee.py

class Employee:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __eq__(self, other):
        return isinstance(other, Employee) and self.name == other.name and self.email == other.email

    def __hash__(self):
        return hash((self.name, self.email))

    def __repr__(self):
        return f"Employee(name={self.name}, email={self.email})"

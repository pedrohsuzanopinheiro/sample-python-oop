class Employee:
    def __init__(self, first: str, last: str, email: str, pay: float) -> None:
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay

    def fullname(self) -> str:
        return f"{self.first} {self.last}"


emp_1 = Employee(
    first="Pedro", last="Pinheiro", email="pedro@pedro.com", pay=100000
)
emp_2 = Employee(
    first="Pedro", last="Junior", email="pedro.junior@pedro.com", pay=10000
)

emps = [emp_1, emp_2]

for emp in emps:
    print(emp.fullname())

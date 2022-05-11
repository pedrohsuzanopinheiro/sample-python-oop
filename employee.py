class Employee:
    num_of_emps = 0
    raise_amount: float = 1.04

    def __init__(self, first: str, last: str, email: str, pay: float) -> None:
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self) -> float:
        return self.pay * self.raise_amount


emp_1 = Employee(
    first="Pedro", last="Pinheiro", email="pedro@pedro.com", pay=100000
)
emp_2 = Employee(
    first="Pedro", last="Junior", email="pedro.junior@pedro.com", pay=75000
)

emp_1.raise_amount = 2

emps = [emp_1, emp_2]

for emp in emps:
    print(emp.fullname(), emp.apply_raise())

print(Employee.num_of_emps)

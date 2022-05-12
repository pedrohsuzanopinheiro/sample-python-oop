import datetime


class Employee:
    num_of_emps: int = 0
    raise_amount: float = 1.04

    def __init__(self, first: str, last: str, pay: float) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self) -> float:
        return self.pay * self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount: float) -> None:
        cls.raise_amount = amount

    @classmethod
    def fromstring(cls, emp_str: str):
        first, last, pay = emp_str.split("-")
        return cls(first=first, last=last, pay=float(pay))

    @staticmethod
    def is_workday(day: datetime) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee(first="Pedro", last="Pinheiro", pay=100000)
emp_2 = Employee(first="Pedro", last="Junior", pay=75000)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"
emp_3 = Employee.fromstring(emp_str_1)
emp_4 = Employee.fromstring(emp_str_2)
emp_5 = Employee.fromstring(emp_str_3)

emps = [emp_1, emp_2, emp_3, emp_4, emp_5]
Employee.set_raise_amt(1.05)

for emp in emps:
    print(emp.fullname(), emp.apply_raise(), emp.raise_amount)

print(Employee.num_of_emps)

today = datetime.datetime.today()
print(f"Is workday? R: {Employee.is_workday(today)}")

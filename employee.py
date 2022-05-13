import datetime
from typing import List


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


class Developer(Employee):
    raise_amount: float = 1.10

    def __init__(
        self, first: str, last: str, pay: float, prog_lang: str
    ) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_amount: float = 1.25

    def __init__(
        self,
        first: str,
        last: str,
        pay: float,
        employees: List[Employee] = None,
    ) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp: Employee) -> None:
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp: Employee) -> None:
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self) -> None:
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer(
    first="Pedro", last="Pinheiro", pay=100000, prog_lang="Python"
)
dev_2 = Developer(first="Pedro", last="Junior", pay=75000, prog_lang="Java")

mgr_1 = Manager(first="Suse", last="Lala", pay=150000, employees=[dev_1])

mgr_1.add_emp(dev_2)

mgr_1.remove_emp(dev_1)

devs = [dev_1, dev_2]

mgr_1.print_emps()

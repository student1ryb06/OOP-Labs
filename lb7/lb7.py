import datetime
class Employee:
    raise_amount = 1.04
    num_of_employees = 0
    def __init__(self, first_name: str, last_name: str, pay: int):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        Employee.num_of_employees += 1
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amount(cls, amount: float):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str: str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))
    @staticmethod
    def is_workday(day: datetime.date):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
if __name__ == "__main__":
    emp_1 = Employee("Іван", "Петренко", 50000)
    emp_2 = Employee("Ольга", "Ковальчук", 60000)
    print(f"Початковий коефіцієнт: {Employee.raise_amount}")
    Employee.set_raise_amount(1.05)
    print(f"Новий коефіцієнт: {Employee.raise_amount}")
    emp_1.apply_raise()
    print(f"\nЗарплата Івана після підвищення: {emp_1.pay}")
    print("-" * 30)
    emp_str_3 = 'Сергій-Мельник-72000'
    emp_3 = Employee.from_string(emp_str_3)
    print("Працівник, створений з рядка:")
    print(f"Ім'я: {emp_3.full_name()}, Зарплата: {emp_3.pay}")
    print(f"Загальна кількість працівників: {Employee.num_of_employees}")
    print("-" * 30)
    my_date = datetime.date(2025, 9, 27)  # Субота
    is_working = "Так" if Employee.is_workday(my_date) else "Ні"
    print(f"Чи є {my_date} робочим днем? - {is_working}")

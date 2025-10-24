class Employee:
    raise_amount = 1.04
    num_of_employees = 0
    def __init__(self, first_name: str, last_name: str, pay: int):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
        Employee.num_of_employees += 1
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
print(f"Початкова кількість працівників: {Employee.num_of_employees}")
emp_1 = Employee("Іван", "Петренко", 50000)
emp_2 = Employee("Ольга", "Ковальчук", 60000)
print(f"Кінцева кількість працівників: {Employee.num_of_employees}")
print("-" * 20)
print("Виклик методу через об'єкт:")
print(emp_1.full_name())
print("\nВиклик методу через клас:")
print(Employee.full_name(emp_1))
print("-" * 20)
print(f"Зарплата Івана до підвищення: {emp_1.pay}")
emp_1.apply_raise()
print(f"Зарплата Івана після підвищення: {emp_1.pay}")

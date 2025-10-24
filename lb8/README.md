**Міністерство освіти та науки України**
**Північний кампус Львівського національного університету ветеринарної медицини та біотехнологій імені С.З. Ґжицького**
**Факультет механіки, енергетики та інформаційних технологій**

# Лабораторна робота №8
## З дисципліни «Об’єктно-орієнтоване програмування»

[cite_start]**Тема:** «Наслідування в об’єктно-орієнтованому програмуванні» [cite: 107]

**Виконала:** студентка групи КН-31з
[cite_start]Рибка Л.Г. [cite: 108-109]

**Перевірив:** 
[cite_start]Татомир А.В. [cite: 110-111]

Львів 2025

---

## Мета
[cite_start]Опанувати концепцію наслідування класів в Python, навчитися створювати батьківські та дочірні класи, перевикористовувати існуючий код, а також використовувати функцію `super()` для доступу до методів батьківського класу. [cite: 113]

---

## Хід роботи
1.  [cite_start]Створено базовий клас `Employee`, що містить загальні атрибути та методи для всіх працівників. [cite: 115]
2.  [cite_start]Створено дочірній клас `Developer`, який успадковує функціонал від класу `Employee`. [cite: 116]
3.  [cite_start]В дочірньому класі `Developer` додано нові атрибути та модифіковано конструктор, використовуючи функцію `super().__init__()` для коректної ініціалізації батьківського класу. [cite: 117]
4.  [cite_start]Результати виконання роботи завантажено до хмарного репозиторію GitHub. [cite: 118]

---

## 1) Код програми
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

    def __repr__(self):
        return f"Employee('{self.first_name}', '{self.last_name}', {self.pay})"

    def __str__(self):
        return f"Працівник: {self.full_name()} - {self.email}, Зарплата: {self.pay}"

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name: str, last_name: str, pay: int, prog_lang: str):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang

    def __repr__(self):
        return f"Developer('{self.first_name}', '{self.last_name}', {self.pay}, '{self.prog_lang}')"

    def __str__(self):
        return (f"Розробник: {self.full_name()} - {self.email}, Зарплата: {self.pay}, "
                f"Мова програмування: {self.prog_lang}")

class Manager(Employee):
    def __init__(self, first_name: str, last_name: str, pay: int, employees=None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        """Додає працівника до списку тих, ким керує менеджер."""
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        """Видаляє працівника зі списку тих, ким керує менеджер."""
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        """Виводить список працівників, якими керує менеджер."""
        if not self.employees:
            print(f"{self.full_name()} не керує жодними працівниками.")
            return
        
        print(f"\nПрацівники, якими керує {self.full_name()}:")
        for emp in self.employees:
            print(f"--> {emp.full_name()}")

    def __repr__(self):
        return f"Manager('{self.first_name}', '{self.last_name}', {self.pay}, {self.employees})"

    def __str__(self):
        return f"Менеджер: {self.full_name()} - {self.email}, Зарплата: {self.pay}"

if __name__ == "__main__":
    emp_1 = Employee("Іван", "Петренко", 50000)
    dev_1 = Developer("Ольга", "Ковальчук", 60000, "Python")
    dev_2 = Developer("Сергій", "Мельник", 70000, "Java")
    
    print(f"Кількість працівників: {Employee.num_of_employees}")
    print("-" * 30)
    
    print(f"Зарплата Івана до підвищення: {emp_1.pay}")
    emp_1.apply_raise()
    print(f"Зарплата Івана після підвищення ({Employee.raise_amount * 100:.0f}%): {emp_1.pay}")
    
    print(f"\nЗарплата Ольги до підвищення: {dev_1.pay}")
    dev_1.apply_raise()
    print(f"Зарплата Ольги після підвищення ({Developer.raise_amount * 100:.0f}%): {dev_1.pay}")
    
    print("-" * 30)
    print(f"Інформація про розробника Ольгу: {dev_1}")
    print(f"Мова програмування Ольги: {dev_1.prog_lang}")
    
    print("-" * 30)
    mgr_1 = Manager("Андрій", "Сидоренко", 90000, [dev_1])
    print(f"Інформація про менеджера: {mgr_1}")
    
    mgr_1.print_employees()
    mgr_1.add_employee(dev_2)
    mgr_1.add_employee(emp_1)
    mgr_1.print_employees()
    mgr_1.remove_employee(dev_1)
    mgr_1.print_employees()
    
    print("-" * 30)
    print(f"Чи є dev_1 екземпляром Developer? {isinstance(dev_1, Developer)}")
    print(f"Чи є dev_1 екземпляром Employee? {isinstance(dev_1, Employee)}")
    print(f"Чи є dev_1 екземпляром Manager? {isinstance(dev_1, Manager)}")
    
    print(f"\nЧи є Developer підкласом Employee? {issubclass(Developer, Employee)}")
    print(f"Чи є Manager підкласом Employee? {issubclass(Manager, Employee)}")
    print(f"Чи є Developer підкласом Manager? {issubclass(Developer, Manager)}")

    ## 2) Висновок
    Під час виконання роботи було досягнуто мети: я опанувала концепцію наслідування в Python. На практиці було створено ієрархію класів (Employee, Developer, Manager), де я навчилася перевикористовувати код за допомогою super().__init__(). Також було застосовано функції isinstance() та issubclass() для перевірки відносин між класами та закріплено навички використання Git для версійного контролю.
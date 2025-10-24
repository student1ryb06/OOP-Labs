**Міністерство освіти та науки України**
**Північний кампус Львівського національного університету ветеринарної медицини та біотехнологій імені С.З. Ґжицького**
**Факультет механіки, енергетики та інформаційних технологій**

# Лабораторна робота №5
## З дисципліни «Об’єктно-орієнтоване програмування»

**Тема:** «Створення та використання класів»

**Виконала:** студентка групи КН-31з
Рибка Л.Г.

**Перевірив:** 
Татомир А.В.

Львів 2025

---

## Мета
Ознайомитися з поняттями класів та об’єктів та закріпити на практиці методи їх створення та використання.

---

## Хід роботи
1.  Встановлено середовище розробки VS Code та інтерпретатор Python 3 на ОС Windows.
2.  Проаналізовано базовий приклад класу «Employee» та визначено розширення функціоналу.
3.  Встановлено систему контролю версій Git.
4.  За допомогою команд «git status, pwd, ls, mkdir, git diff --staged, git commit -m "message"» та інших збережено програму в локальному репозиторії.
5.  Підключено результати лабораторної роботи до хмарного репозиторію GitHub.

---

## Код програми
class Employee:
    raise_amount = 1.05
    num_of_employees = 0
    all_employees = []

    def __init__(self, first_name: str, last_name: str, salary: int):
        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError("Ім'я не може бути порожнім.")
        if not isinstance(last_name, str) or not last_name.strip():
            raise ValueError("Прізвище не може бути порожнім.")
        if not isinstance(salary, (int, float)) or salary <= 0:
            raise ValueError("Зарплатня повинна бути додатним числом.")
        
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.salary = salary
        
        Employee.num_of_employees += 1
        Employee.all_employees.append(self)

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@company.com'

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    def __repr__(self):
        return f"Employee('{self.first_name}', '{self.last_name}', {self.salary})"

    def __str__(self):
        return f"Працівник: {self.fullname} - {self.email}"

if __name__ == "__main__":
    emp_1 = Employee('Іван', 'Петренко', 50000)
    emp_2 = Employee('Олена', 'Ковальчук', 65000)
    emp_3 = Employee('Сергій', 'Мельник', 72000)
    
    print(f"Загальна кількість працівників: {Employee.num_of_employees}")
    
    print("Список працівників:")
    for emp in Employee.all_employees:
        print(f"- {emp.fullname}")
    
    print("\n--- Детальна інформація ---")
    print(emp_1)
    print(f"Зарплатня: {emp_1.salary}")
    emp_1.apply_raise()
    print(f"Нова зарплатня: {emp_1.salary}")
    
    try:
        emp_invalid = Employee("Тест", "Тест", -100)
    except ValueError as e:
        print(f"\nПомилка створення об'єкта: {e}")

        ### Висновок
        Під час виконання лабораторної роботи я ознайомилася з поняттями класів та об'єктів у Python і закріпила їх практичне використання. Було створено клас Employee з конструктором та перевіркою вхідних даних, а також властивостями (@property) для автоматичної генерації полів email та fullname. Робота дозволила поглибити знання про інкапсуляцію та обробку даних у класах.
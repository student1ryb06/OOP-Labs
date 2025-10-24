class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@email.com'
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print('Deleting Name!')
        self.first = None
        self.last = None
emp_1 = Employee('John', 'Smith')
print(f"Початкове ім'я: {emp_1.first}")
print(f"Початковий email: {emp_1.email}")
print(f"Повне ім'я: {emp_1.fullname}\n")
emp_1.first = 'Jim'
print(f"Нове ім'я: {emp_1.first}")
print(f"Новий email (динамічно оновився): {emp_1.email}")
print(f"Нове повне ім'я: {emp_1.fullname}\n")
emp_1.fullname = 'Jane Doe'
print(f"Ім'я після використання сеттера: {emp_1.first}")
print(f"Прізвище після використання сеттера: {emp_1.last}")
print(f"Повне ім'я: {emp_1.fullname}")
print(f"Email оновився автоматично: {emp_1.email}\n")
del emp_1.fullname
print(f"Ім'я після видалення: {emp_1.first}")
print(f"Прізвище після видалення: {emp_1.last}")


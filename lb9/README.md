**Міністерство освіти та науки України**
**Північний кампус Львівського національного університету ветеринарної медицини та біотехнологій імені С.З. Ґжицького**
**Факультет механіки, енергетики та інформаційних технологій**

# Лабораторна робота №9
## З дисципліни «Об’єктно-орієнтоване програмування»

[cite_start]**Тема:** «Поліморфізм в Python 3» [cite: 417]

**Виконала:** студентка групи КН-31з
[cite_start]Рибка Л.Г. [cite: 418-419]

**Перевірив:** 
[cite_start]Татомир А.В. [cite: 420-421]

Львів 2025

---

## Мета
[cite_start]Засвоїти застосування принципу поліморфізму в об’єктномо-орієнтованому програмуванні. [cite: 423]

---

## Хід роботи
1.  [cite_start]Створено клас `Employee` з атрибутами `first` та `last` та методами для отримання і зміни повного імені (`fullname`) і `email`. [cite: 425]
2.  [cite_start]Продемонстровано динамічне оновлення `email` при зміні імені та використання сеттера і делетера для `fullname`. [cite: 426]
3.  [cite_start]Перевірено роботу класу на об’єкті `emp_1` через вивід початкових та змінених значень атрибутів. [cite: 427]
4.  [cite_start]Код завантажено на GitHub через локальний репозиторій, зроблено коміти та підключено віддалений репозиторій. [cite: 428]

---

## 1) Код програми
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

---

## 2) Висновок
Під час лабораторної роботи я ознайомилася з принципом поліморфізму в Python, закріпила використання властивостей класу (@property, сеттер, делетер) для динамічного керування атрибутами об’єкта та навички роботи з Git та GitHub для збереження та публікації коду.
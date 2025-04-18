"""Создать класс Person с атрибутами
    - имя,
    - дата рождения,
    - рост (в метрах)
    - вес (в килограммах)
    и методами для вычисления
        - возраста
                birth_day = "2000-01-30"
                birthdate = datetime.strptime(birth_day, '%Y-%m-%d').date()
                today = datetime.today().date()
                age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        - индекса массы тела
                BMI = weight / (height ** 2)

Рост и вес при создании класса являются необязательными.
Если хотя бы из этих параметров отсутствует - индекс массы тела возвращает None
Создать конструкторы от разного числа аргументов.
Переопределить методы __str__, __repr__.
"""

from datetime import datetime


def get_age(self):
birthdate = datetime.strptime(self.birth_day, '%Y-%m-%d').date()
today = datetime.today().date()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
return age



person1 = Person('Alice', '1990-05-15')
person2 = Person('Bob', '1985-05-15', 1.75, 70)

print(person1)
print(repr(person1))
print(f"Возраст {person1.name}: {person1.get_age()} лет")
print(f"BMI {person1.name}: {person1.get_bmi()}")

print(person2)
print(repr(person2))
print(f"Возраст {person2.name}: {person2.get_age()} лет")
print(f"BMI {person2.name}: {person2.get_bmi():.2f}")

# Person(name=Alice, birth_year=1990, height=None, weight=None)
# Person('Alice', 1990, None, None)
# Возраст Alice: 34 лет
# BMI Alice: None

# Person(name=Bob, birth_year=1985, height=1.75, weight=70)
# Person('Bob', 1985, 1.75, 70)
# Возраст Bob: 39 лет
# BMI Bob: 22.86

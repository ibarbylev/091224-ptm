"""БД и запросы на изменение"""

# Подключение библиотеки, соответствующей типу требуемой базы данных
import os
import sqlite3

connection = sqlite3.connect("demo.sqlite")
cursor = connection.cursor()

# Узнаём число записей до изменения
cursor.execute('SELECT COUNT(*) FROM Artist;')
print('rows', cursor.fetchone())

# ---------------------------Запрос на изменение----------------------------- #
cursor.execute("INSERT INTO Artist VALUES (Null, 'A') ;")
connection.commit()

# Проверка результатов
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
result = cursor.fetchall()
print(result)  # -> [('A',), ('A Cor Do Som',), ('AC/DC',)]

cursor.execute('SELECT COUNT(*) FROM Artist;')
print('rows', cursor.fetchone())


cursor.close()
connection.close()

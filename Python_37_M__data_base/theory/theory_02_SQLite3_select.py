"""БД и запросы на выборку"""


# 1. Необходимо подключить (импортировать_ библиотеку, соответствующую вашей БД
import sqlite3

# 2. Установить постоянное соединение с БД
connection = sqlite3.connect("demo.sqlite")

# 3. Создать объект для управления БД
cursor = connection.cursor()
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")

# 4. Извлечение информации из курсора
# ВАЖНО: cursor - это итератора (обратиться к нему только ОДИН раз!)
# cursor.fetchall() - возвращает все записи выборки
# cursor.fetchone() - возвращает одну запись
# cursor.fetchmany(n) - возвращает n записей

print('data =', cursor.fetchall())
# [('A Cor Do Som',), ('AC/DC',), ('Aaron Copland & London Symphony Orchestra',)]


# Повторное обращение к объекту cursor вернёт пустой список
print('data =', cursor.fetchall())
# []

print('------------ fetchone() ------------------')

cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

"""
('A Cor Do Som',)
('AC/DC',)
('Aaron Copland & London Symphony Orchestra',)
None

---------------------------
Как видим, последний запрос вернул None, означающий, 
что все данные из объекта cursor уже извлечены
"""

print('------------ fetchmany(2) ------------------')
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
print('data =', cursor.fetchmany(2))

cursor.close()
connection.close()

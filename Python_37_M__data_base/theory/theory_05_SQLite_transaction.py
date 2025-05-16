"""БД и запросы на изменение"""

# Подключение библиотеки, соответствующей типу требуемой базы данных
import os
import sqlite3

connection = sqlite3.connect("demo.sqlite")
cursor = connection.cursor()


try:
    # ---------------------------Запрос на изменение----------------------------- #
    cursor.executemany(
        "INSERT INTO Artist VALUES (?, ?)",
        [(None, 'No_name_1'), (None, 'No_name_2'), (None, 'No_name_3')]
    )
    connection.commit()


except Exception as e:
    connection.rollback()
    print(e)

finally:
    cursor.close()
    connection.close()





#  pip install mysql-connector-python

import mysql.connector
from local_settings import HOST, USER, PASSWORD, DATABASE

dbconfig = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DATABASE,
}

with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:

        # Получение списка таблиц
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        # Вывод списка таблиц
        print("Список таблиц в базе данных:")
        for table in tables:
            print(table[0])




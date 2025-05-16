#  pip install mysql-connector-python

import mysql.connector
from local_settings import HOST, USER, PASSWORD

dbconfig = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': '250324_dam_Python',
}

with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:

        cursor.executemany(
            "INSERT INTO Artist (Artist, age) VALUES (%s, %s)",
            [('No_name_1', 50), ('No_name_2', 30), ('No_name_3', 25)]
        )
        connection.commit()




"""Получить спислок
"""

import mysql.connector
from local_settings_edit import dbconfig


class MySQLConnection:
    def __init__(self, db_config):
        self.dbconfig = db_config
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.dbconfig)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def show_databases(self):
        try:
            self.cursor.execute("SHOW DATABASES;")
            result = self.cursor.fetchall()
            for x in result:
                dbname = x[0]
                if '050824' in dbname:
                    print(dbname)
        except Exception as e:
            print(e)

    def show_table(self, table_name: str, is_show: bool = False) -> list | None:
        """Возвращает содержимое таблицы (list[tuple[str,...]])
        по имени таблицы table_name.

        Дополнительно: (is_show=True) выводит содержимое таблицы на экран.
        """
        try:
            # Проверка наличия таблицы
            self.cursor.execute("SHOW TABLES;")
            all_tables = [row[0] for row in self.cursor.fetchall()]

            if table_name not in all_tables:
                raise ValueError(f"Таблица '{table_name}' не существует в базе данных.")

            # Получение всех данных из таблицы
            self.cursor.execute(f"SELECT * FROM `{table_name}`;")
            rows = self.cursor.fetchall()

            if is_show:
                print(f"Содержимое таблицы '{table_name}':")
                for row in rows:
                    print(row)

            return rows

        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")
            return None

    def show_tables(self, database_name: str) -> None:
        try:
            self.cursor.execute(f"USE {database_name};")

            # Получение списка таблиц
            self.cursor.execute("SHOW TABLES;")
            result = self.cursor.fetchall()
            for x in result:
                print(x[0])

        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")

    def dump_import(self, dump_path, database_name):
        try:
            with open(dump_path, "r", encoding="utf-8") as file:
                dump_content = file.read()

            commands = dump_content.split(";")

            self.cursor(f"USE {database_name}")

            for command in commands:
                command = command.strip()  # Удаляем лишние пробелы и переносы строк
                if command:  # Пропускаем пустые команды
                    try:
                        self.cursor.execute(command)
                        print(f"Выполнено: {command[:50]}...")
                    except mysql.connector.Error as err:
                        print(f"Ошибка при выполнении команды: {command[:50]}...\n{err}")

            # Сохранение изменений (на всякий случай
            self.connection.commit()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    with MySQLConnection(dbconfig) as db_manager:
        db_manager.show_databases()
        db_manager.show_tables("050824_BAR_sakila")



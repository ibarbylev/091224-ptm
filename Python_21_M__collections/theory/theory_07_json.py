import json

# Сериализация Python-объекта в JSON-строку
data: dict = {"name": "John", "age": 25, "city": "New York"}
json_str: str = json.dumps(data)
print(json_str)  # Выводит '{"name": "John", "age": 25, "city": "New York"}'

""" =============>> ОТПРАВКА ДАННЫХ ПО КАНАЛУ СВЯЗИ В ВИДЕ ТЕКСТА ===============>> """


""" <<============= ПОЛУЧЕНИЕ ДАННЫХ ПО КАНАЛУ СВЯЗИ В ВИДЕ ТЕКСТА <<=============== """

# Десериализация JSON-строки в Python-объект
json_str: str = '{"name": "John", "age": 25, "city": "New York"}'
data: dict = json.loads(json_str)
print(data["name"])  # Выводит 'John'


""" ============== Запись и чтение  json файла ==================== """

with open("theory_07_json.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


with open("theory_07_json.json", "r", encoding="utf-8") as f:
    person: dict = json.load(f)
    print(person)

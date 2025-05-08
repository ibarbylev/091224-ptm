"""Протоколы (Protocols)
Протокол — это способ определения требований к объектам,
которые должны предоставлять определённые методы или атрибуты, но не обязательно через наследование.
Протоколы описывают поведение объектов, а не их структуру.
То есть, похожи на аннотацию типов:
    - содержит скорее не требования, а пожелания, отсутствие которых не вызывает ошибку.
    - поэтому проверяются статистическим анализом в IDE (как аннотации)
    - либо специальными пакетами, например mypy

mypy:
    - требуется предварительная установка:
        pip install mypy

    - проверка файла на соответствие требованиям протокола:
        mypy my_filename.py

    - в случае соответствия выдаст примерно следующее:
        Success: no issues found in 1 source file

    - а в случае несоответствия:
        error: Argument 1 to "save_to_storage" has incompatible type "BadSerializer"; expected "Serializer"
        note: "BadSerializer" is missing method "serialize"

"""

from typing import Protocol


class Serializer(Protocol):
    def serialize(self) -> str:
        pass


class JSONData:
    def serialize(self) -> str:
        return '{"key": "value"}'


class BadSerializer:
    def save(self) -> str:
        return "saving..."


def save_to_storage(obj: Serializer):
    print(obj)


json_data = JSONData()
bad_obj = BadSerializer()
save_to_storage(json_data)
save_to_storage(bad_obj)  # PyCharm подсвечивает ошибку, но runtime её не выдаст (в отличии от Abstract class)

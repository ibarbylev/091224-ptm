"""Сгенерировать все пароли, состоящие из 4 символов чтобы среди них была хотя бы
  - одна большая латинская буква,
  - одна маленькая,
  - одна цифра и никаких иных типов символов.
При этом запрещено, чтобы символ повторялся в пароле или две соседние по алфавиту буквы стояли рядом.
Записать полученные пароли в файл.

Generated 4557072 valid passwords and saved to file.
"""
import itertools
import json

POSSIBLE_SYMBOLS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def has_required_characters(password: str) -> bool:
    """Check if the password has at least one uppercase, one lowercase, and one digit."""
    pass


def has_no_repeated_or_sequential_characters(password: str) -> bool:
    """Check if the password has no repeated or sequential characters."""
    pass


def is_valid_password(password: str) -> bool:
    """Check if the password is valid based on the given rules."""
    pass


def generate_passwords(characters: str) -> list[str]:
    """Generate all valid passwords."""
    pass


def write_passwords_to_file(passwords: list[str], filename="tmp.json"):
    """Write the passwords to a file."""
    pass


if __name__ == "__main__":
    valid_passwords = generate_passwords(POSSIBLE_SYMBOLS)
    write_passwords_to_file(valid_passwords)
    print(f"Generated {len(valid_passwords)} valid passwords and saved to file.")

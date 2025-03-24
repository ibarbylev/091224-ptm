from typing import List, Tuple, Set, Dict, Union


def process_data(data: List[str]) -> Tuple[int, Set[str]]:
    return len(data), set(data)


def get_person_details(person: Dict[str, Union[str, int]]) -> str:
    return f"{person['name']}, {person['age']} years old"


# ========= variant 2 ==========
def process_data_2(data: list[str]) -> tuple[int, set[str]]:
    return len(data), set(data)


def get_person_details_2(person: dict[str, str | int]) -> str:
    return f"{person['name']}, {person['age']} years old"

from typing import Iterator, Generator


def make_iterator(lst: list[int]) -> Iterator[int]:
    return iter(lst)


# Generator[yield_type, send_type, return_type]
def generate_numbers(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i

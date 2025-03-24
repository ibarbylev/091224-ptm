from typing import Optional, Union, Any


def greet(name: Optional[str]) -> Union[str, int]:
    if name is None:
        return "Hello, anonymous"
    else:
        return f"Hello, {name}"


greet()
greet('5')
greet(5555)


# Variant 2


def greet_2(name: str | None) -> str | int:
    if name is None:
        return "Hello, anonymous"
    else:
        return f"Hello, {name}"




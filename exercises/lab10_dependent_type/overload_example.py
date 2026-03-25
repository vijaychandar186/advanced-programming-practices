"""
Lab 10 – Dependent Type Programming
Program C: Demonstrate @overload decorator for type-dependent dispatch.
"""

from typing import Union, overload


@overload
def process(value: int) -> str: ...
@overload
def process(value: str) -> int: ...

def process(value: Union[int, str]) -> Union[str, int]:
    if isinstance(value, int):
        return f"Got integer: {value}"
    return len(value)


@overload
def add(a: int, b: int) -> int: ...
@overload
def add(a: str, b: str) -> str: ...

def add(a, b):
    return a + b


if __name__ == "__main__":
    print(process(42))
    print(process("hello"))
    print(add(3, 4))
    print(add("foo", "bar"))

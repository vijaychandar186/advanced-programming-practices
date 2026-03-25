"""
Lab 10 – Dependent Type Programming
Program A: Demonstrate Union types.
"""

from typing import Union


def process(value: Union[int, float, str]) -> str:
    if isinstance(value, int):
        return f"Integer: {value}  (squared: {value ** 2})"
    if isinstance(value, float):
        return f"Float: {value:.4f}  (halved: {value / 2:.4f})"
    return f"String: '{value}'  (upper: '{value.upper()}')"


if __name__ == "__main__":
    samples: list[Union[int, float, str]] = [42, 3.14159, "hello"]
    for s in samples:
        print(process(s))

"""
Lab 07 – Functional Programming
Program A: Use map() to double the numbers {2, 4, 6, 8} and then double
them again.
"""


def double_twice(numbers):
    doubled     = list(map(lambda x: x * 2, numbers))
    quadrupled  = list(map(lambda x: x * 2, doubled))
    return doubled, quadrupled


if __name__ == "__main__":
    numbers = [2, 4, 6, 8]
    doubled, quadrupled = double_twice(numbers)
    print(f"Original:      {numbers}")
    print(f"Doubled:       {doubled}")
    print(f"Doubled again: {quadrupled}")

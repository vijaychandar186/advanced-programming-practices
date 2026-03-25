"""
Lab 07 – Functional Programming
Program C: Calculate the first 11 Fibonacci numbers and filter out the odd
and even elements separately.
"""


def fibonacci(n):
    fibs = [0, 1]
    for _ in range(n - 2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]


def filter_odd_even(sequence):
    odds  = list(filter(lambda x: x % 2 != 0, sequence))
    evens = list(filter(lambda x: x % 2 == 0, sequence))
    return odds, evens


if __name__ == "__main__":
    fibs = fibonacci(11)
    odds, evens = filter_odd_even(fibs)
    print(f"First 11 Fibonacci numbers: {fibs}")
    print(f"Odd  Fibonacci numbers:     {odds}")
    print(f"Even Fibonacci numbers:     {evens}")

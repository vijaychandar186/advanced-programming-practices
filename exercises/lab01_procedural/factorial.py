"""
Lab 01 – Procedural Programming
Program A: Find the factorial of a given number.
"""


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Factorial of {n} is {factorial(n)}")

"""
Lab 02 – Structural Programming
Program C: Find the greatest of three numbers.
"""


def greatest_of_three(a, b, c):
    return max(a, b, c)


if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    print(f"Greatest: {greatest_of_three(a, b, c)}")

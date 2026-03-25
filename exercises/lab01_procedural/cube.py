"""
Lab 01 – Procedural Programming
Program B: Calculate the cube of a number using def() and lambda().
"""


def cube(n):
    return n ** 3


cube_lambda = lambda n: n ** 3


if __name__ == "__main__":
    n = float(input("Enter a number: "))
    print(f"Cube using def:    {cube(n)}")
    print(f"Cube using lambda: {cube_lambda(n)}")

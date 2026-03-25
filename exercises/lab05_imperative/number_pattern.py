"""
Lab 05 – Imperative Programming
Program A: Print the following pattern for n rows:
  1
  2 2
  3 3 3
  ...
"""


def print_pattern(n):
    for i in range(1, n + 1):
        print(" ".join([str(i)] * i))


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print_pattern(n)

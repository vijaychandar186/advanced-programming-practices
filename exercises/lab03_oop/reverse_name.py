"""
Lab 03 – Object-Oriented Programming
Program B: Accept a user's first and last name and print them in reverse
order with a space between them.
"""


class NameReverser:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def reversed_name(self):
        return f"{self.last} {self.first}"


if __name__ == "__main__":
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    nr = NameReverser(first, last)
    print(nr.reversed_name())

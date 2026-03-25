"""
Lab 03 – Object-Oriented Programming
Program A: Ask the user for their name and age, then print the year they
will turn 100 years old.
"""

import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def year_turns_100(self):
        current_year = datetime.datetime.now().year
        return current_year + (100 - self.age)


if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    p = Person(name, age)
    print(f"{p.name}, you will turn 100 in the year {p.year_turns_100()}.")

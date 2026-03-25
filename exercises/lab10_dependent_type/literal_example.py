"""
Lab 10 – Dependent Type Programming
Program B: Demonstrate Literal types.
"""

from typing import Literal

Direction = Literal["north", "south", "east", "west"]
Status    = Literal["active", "inactive", "pending"]


def move(direction: Direction, steps: int) -> str:
    return f"Moving {steps} step(s) {direction}."


def status_message(status: Status) -> str:
    messages: dict[Status, str] = {
        "active":   "System is running.",
        "inactive": "System is stopped.",
        "pending":  "System is starting up.",
    }
    return messages[status]


if __name__ == "__main__":
    print(move("north", 5))
    print(move("east",  3))
    print(status_message("active"))
    print(status_message("pending"))

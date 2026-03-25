"""
Lab 02 – Structural Programming
Program A: Create a third list containing odd numbers from list1 and even
numbers from list2.
"""


def merge_odd_even(list1, list2):
    odds  = [x for x in list1 if x % 2 != 0]
    evens = [x for x in list2 if x % 2 == 0]
    return odds + evens


if __name__ == "__main__":
    list1 = list(map(int, input("Enter first list (space-separated integers): ").split()))
    list2 = list(map(int, input("Enter second list (space-separated integers): ").split()))
    result = merge_odd_even(list1, list2)
    print(f"Result: {result}")

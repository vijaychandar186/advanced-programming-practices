"""
Lab 01 – Procedural Programming
Program C: Return the number of times "Emma" appears in a given string.
"""


def count_emma(s):
    count = 0
    start = 0
    while True:
        pos = s.find("Emma", start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
    return count


if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"'Emma' appears {count_emma(s)} time(s)")

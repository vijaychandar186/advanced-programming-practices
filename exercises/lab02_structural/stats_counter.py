"""
Lab 02 – Structural Programming
Program B: Read integers until 0, count positives/negatives, compute total
and average (excluding zeros).
"""


def compute_stats():
    positives = negatives = 0
    total = 0.0
    count = 0

    while True:
        try:
            n = int(input("Enter an integer (0 to quit): "))
        except EOFError:
            break
        if n == 0:
            break
        if n > 0:
            positives += 1
        else:
            negatives += 1
        total += n
        count += 1

    avg = total / count if count > 0 else 0.0
    print(f"Positives: {positives}")
    print(f"Negatives: {negatives}")
    print(f"Total: {total}")
    print(f"Average: {avg:.2f}")


if __name__ == "__main__":
    compute_stats()

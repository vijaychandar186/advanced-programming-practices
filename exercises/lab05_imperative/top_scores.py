"""
Lab 05 – Imperative Programming
Program B: Read student scores and display the highest and second-highest.
"""


def find_top_two(scores):
    top1 = top2 = float('-inf')
    for s in scores:
        if s > top1:
            top2 = top1
            top1 = s
        elif s > top2:
            top2 = s
    return top1, top2


if __name__ == "__main__":
    n = int(input("Enter number of students: "))
    scores = []
    for i in range(n):
        score = float(input(f"Enter score for student {i + 1}: "))
        scores.append(score)

    if len(scores) < 2:
        print("Need at least 2 scores.")
    else:
        top1, top2 = find_top_two(scores)
        print(f"Highest score:        {top1}")
        print(f"Second highest score: {top2}")

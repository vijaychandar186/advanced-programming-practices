"""
Lab 05 – Imperative Programming
Program C: Compute university tuition ten years from now (5% annual increase)
and the total cost of four years starting ten years from now.
Base tuition: $10,000 (year 0).
"""


def compute_tuition(base=10_000.0, rate=0.05):
    tuition = base
    for _ in range(10):
        tuition *= 1 + rate
    year_10 = tuition
    total_4yr = sum(tuition * (1 + rate) ** i for i in range(4))
    return year_10, total_4yr


if __name__ == "__main__":
    year_10, total_4yr = compute_tuition()
    print(f"Tuition in 10 years:                         ${year_10:,.2f}")
    print(f"Total 4-year cost starting 10 years from now: ${total_4yr:,.2f}")

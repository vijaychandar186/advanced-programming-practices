"""
Lab 14 – Symbolic Programming
Program B: Compute 1st–4th order derivatives of sin(2x^3 - 9x) using SymPy.
"""

try:
    from sympy import symbols, sin, diff, simplify
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False


def run_derivatives():
    if not HAS_SYMPY:
        print("sympy not installed.")
        print("Derivatives of f(x) = sin(2x^3 - 9x):")
        print("  1st: (6x^2 - 9)*cos(2x^3 - 9x)")
        print("  2nd: ...")
        return

    x = symbols("x")
    f = sin(2 * x**3 - 9 * x)
    print(f"f(x) = {f}\n")

    for order in range(1, 5):
        d = simplify(diff(f, x, order))
        print(f"  d^{order}/dx^{order} f = {d}")


if __name__ == "__main__":
    run_derivatives()

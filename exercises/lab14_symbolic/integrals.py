"""
Lab 14 – Symbolic Programming
Program C: Compute definite and indefinite integrals using SymPy's integrate().
"""

try:
    from sympy import symbols, integrate, sin, exp, pi
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False


def run_integrals():
    if not HAS_SYMPY:
        print("sympy not installed.")
        return

    x = symbols("x")

    indefinite = [
        (x**2 + 3 * x,  "x^2 + 3x"),
        (sin(x),         "sin(x)"),
        (exp(x),         "e^x"),
    ]

    print("Indefinite Integrals:")
    for expr, label in indefinite:
        result = integrate(expr, x)
        print(f"  ∫ {label} dx = {result} + C")

    definite = [
        (x**2, x, 0, 3,  "x^2  from 0 to 3"),
        (sin(x), x, 0, pi, "sin(x) from 0 to π"),
    ]

    print("\nDefinite Integrals:")
    for expr, var, a, b, label in definite:
        result = integrate(expr, (var, a, b))
        print(f"  ∫ {label} = {result}")


if __name__ == "__main__":
    run_integrals()

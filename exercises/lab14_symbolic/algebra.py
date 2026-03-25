"""
Lab 14 – Symbolic Programming
Program A: Perform expand(), factor(), and simplify() using SymPy.
  expand  : (a + b)^2
  factor  : a^2 + 2ab + b^2
  simplify: 2x^2 + x(4x + 3)
"""

try:
    from sympy import symbols, expand, factor, simplify
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False


def run_algebra():
    if not HAS_SYMPY:
        print("sympy not installed — showing expected results:")
        print("  expand((a+b)^2)         = a**2 + 2*a*b + b**2")
        print("  factor(a**2+2*a*b+b**2) = (a + b)**2")
        print("  simplify(2*x**2 + x*(4*x+3)) = 6*x**2 + 3*x")
        return

    a, b, x = symbols("a b x")

    expr1 = (a + b) ** 2
    expanded = expand(expr1)
    print(f"Expression:  (a + b)^2")
    print(f"  expand:    {expanded}")
    print(f"  factor:    {factor(expanded)}")

    expr2 = 2 * x**2 + x * (4 * x + 3)
    print(f"\nExpression:  2x^2 + x(4x + 3)")
    print(f"  simplify:  {simplify(expr2)}")


if __name__ == "__main__":
    run_algebra()

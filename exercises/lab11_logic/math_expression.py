"""
Lab 11 – Logic Programming
Program A: Match mathematical expressions using regular expressions.
"""

import re

PATTERNS = {
    "addition":       re.compile(r"^(\d+)\s*\+\s*(\d+)$"),
    "subtraction":    re.compile(r"^(\d+)\s*-\s*(\d+)$"),
    "multiplication": re.compile(r"^(\d+)\s*\*\s*(\d+)$"),
    "division":       re.compile(r"^(\d+)\s*/\s*(\d+)$"),
    "power":          re.compile(r"^(\d+)\s*\^\s*(\d+)$"),
}


def match_expression(expr: str):
    for op, pattern in PATTERNS.items():
        m = pattern.match(expr.strip())
        if m:
            return op, int(m.group(1)), int(m.group(2))
    return None, None, None


if __name__ == "__main__":
    tests = ["3 + 4", "10 - 2", "5 * 6", "8 / 2", "2 ^ 3", "hello world"]
    for expr in tests:
        op, a, b = match_expression(expr)
        if op:
            print(f"'{expr}' → {op}: operands {a} and {b}")
        else:
            print(f"'{expr}' → no match")

"""
Lab 11 – Logic Programming
Program B: Safe evaluation of arithmetic expressions using the AST module.
"""

import ast
import operator

_OPS = {
    ast.Add:  operator.add,
    ast.Sub:  operator.sub,
    ast.Mult: operator.mul,
    ast.Div:  operator.truediv,
    ast.Pow:  operator.pow,
    ast.USub: operator.neg,
}


def safe_eval(expr: str) -> float:
    def _eval(node):
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.BinOp):
            return _OPS[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp):
            return _OPS[type(node.op)](_eval(node.operand))
        raise ValueError(f"Unsupported node: {type(node).__name__}")

    tree = ast.parse(expr, mode="eval")
    return _eval(tree.body)


if __name__ == "__main__":
    expressions = [
        "3 + 4 * 2",
        "(10 - 3) * 2",
        "2 ** 10",
        "100 / 4 + 5",
        "(1 + 2) ** 3",
    ]
    for expr in expressions:
        result = safe_eval(expr)
        print(f"{expr} = {result}")

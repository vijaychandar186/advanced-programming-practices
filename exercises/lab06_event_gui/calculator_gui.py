"""
Lab 06 – Event-Driven & GUI Programming
Program A: Simple calculator using GUI and event handling.
Falls back to CLI when no display is available.
"""


def calculate(expr: str) -> str:
    """Evaluate a numeric expression string safely."""
    allowed = set("0123456789+-*/.() ")
    if not all(c in allowed for c in expr):
        return "Error: invalid characters"
    try:
        result = eval(expr, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {e}"


def run_gui():
    try:
        import tkinter as tk

        root = tk.Tk()
        root.title("Simple Calculator")

        display = tk.StringVar()
        tk.Entry(root, textvariable=display, font=("Arial", 16),
                 width=20, justify="right").grid(row=0, column=0,
                                                  columnspan=4, padx=5, pady=5)

        def btn_click(val):
            if val == "=":
                display.set(calculate(display.get()))
            elif val == "C":
                display.set("")
            else:
                display.set(display.get() + val)

        buttons = ["7", "8", "9", "/",
                   "4", "5", "6", "*",
                   "1", "2", "3", "-",
                   "0", ".", "=", "+", "C"]

        row, col = 1, 0
        for b in buttons:
            tk.Button(root, text=b, width=5, height=2,
                      command=lambda v=b: btn_click(v)).grid(
                          row=row, column=col, padx=2, pady=2)
            col += 1
            if col == 4:
                col = 0
                row += 1

        root.mainloop()

    except Exception:
        print("GUI not available – running in CLI mode.")
        while True:
            try:
                expr = input("Expression (or 'quit'): ").strip()
            except EOFError:
                break
            if expr.lower() == "quit":
                break
            print("=", calculate(expr))


if __name__ == "__main__":
    run_gui()

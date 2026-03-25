"""
Lab 06 – Event-Driven & GUI Programming
Program B: GUI application that greets the user by name.
Falls back to CLI when no display is available.
"""


def greet(name: str) -> str:
    return f"Hello, {name}! Welcome!"


def run_gui():
    try:
        import tkinter as tk

        root = tk.Tk()
        root.title("Greeter")

        tk.Label(root, text="Enter your name:", font=("Arial", 12)).pack(pady=5)
        name_var = tk.StringVar()
        tk.Entry(root, textvariable=name_var, font=("Arial", 12)).pack(pady=5)

        result_var = tk.StringVar()
        tk.Label(root, textvariable=result_var,
                 font=("Arial", 12), fg="blue").pack(pady=5)

        tk.Button(root, text="Greet",
                  command=lambda: result_var.set(greet(name_var.get()))).pack(pady=5)

        root.mainloop()

    except Exception:
        print("GUI not available – running in CLI mode.")
        try:
            name = input("Enter your name: ")
            print(greet(name))
        except EOFError:
            pass


if __name__ == "__main__":
    run_gui()

"""
Lab 06 – Event-Driven & GUI Programming
Program C: Registration form to collect name, email, gender, and PCM marks;
store in SQLite and allow viewing records.
Falls back to CLI when no display is available.
"""

import sqlite3


def setup_db(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            name      TEXT,
            email     TEXT,
            gender    TEXT,
            physics   INTEGER,
            chemistry INTEGER,
            maths     INTEGER
        )
    """)
    conn.commit()


def add_record(conn, name, email, gender, physics, chemistry, maths):
    conn.execute(
        "INSERT INTO registrations (name, email, gender, physics, chemistry, maths) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (name, email, gender, physics, chemistry, maths),
    )
    conn.commit()


def view_records(conn):
    return conn.execute("SELECT * FROM registrations").fetchall()


def run_gui():
    conn = sqlite3.connect(":memory:")
    setup_db(conn)

    try:
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.title("Student Registration")

        field_defs = [
            ("Name",           tk.StringVar()),
            ("Email",          tk.StringVar()),
            ("Gender (M/F)",   tk.StringVar()),
            ("Physics",        tk.StringVar()),
            ("Chemistry",      tk.StringVar()),
            ("Maths",          tk.StringVar()),
        ]

        for i, (label, var) in enumerate(field_defs):
            tk.Label(root, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            tk.Entry(root, textvariable=var).grid(row=i, column=1, padx=5, pady=2)

        def submit():
            vals = [v.get() for _, v in field_defs]
            try:
                add_record(conn, vals[0], vals[1], vals[2],
                           int(vals[3]), int(vals[4]), int(vals[5]))
                messagebox.showinfo("Success", "Record added!")
                for _, v in field_defs:
                    v.set("")
            except ValueError:
                messagebox.showerror("Error", "Marks must be integers.")

        def view():
            rows = view_records(conn)
            top = tk.Toplevel(root)
            top.title("Records")
            headers = ["ID", "Name", "Email", "Gender", "Phy", "Chem", "Math"]
            for j, h in enumerate(headers):
                tk.Label(top, text=h, font=("Arial", 10, "bold")).grid(row=0, column=j, padx=5)
            for i, row in enumerate(rows, 1):
                for j, val in enumerate(row):
                    tk.Label(top, text=str(val)).grid(row=i, column=j, padx=5)

        btn_row = len(field_defs)
        tk.Button(root, text="Submit",       command=submit).grid(row=btn_row, column=0, pady=5)
        tk.Button(root, text="View Records", command=view  ).grid(row=btn_row, column=1, pady=5)
        root.mainloop()

    except Exception:
        print("GUI not available – running in CLI mode.")
        try:
            name      = input("Name: ")
            email     = input("Email: ")
            gender    = input("Gender (M/F): ")
            physics   = int(input("Physics: "))
            chemistry = int(input("Chemistry: "))
            maths     = int(input("Maths: "))
            add_record(conn, name, email, gender, physics, chemistry, maths)
            print("Record added. All records:")
            for row in view_records(conn):
                print(row)
        except EOFError:
            pass

    conn.close()


if __name__ == "__main__":
    run_gui()

"""
Lab 04 – Declarative Programming
Program C: Student database collecting name, gender, email, and PCM marks.
"""

import sqlite3


def setup_db(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            name      TEXT NOT NULL,
            gender    TEXT NOT NULL,
            email     TEXT NOT NULL,
            physics   INTEGER NOT NULL,
            chemistry INTEGER NOT NULL,
            maths     INTEGER NOT NULL
        )
    """)
    conn.commit()


def add_student(conn, name, gender, email, physics, chemistry, maths):
    conn.execute(
        "INSERT INTO students (name, gender, email, physics, chemistry, maths) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (name, gender, email, physics, chemistry, maths),
    )
    conn.commit()


def list_students(conn):
    cur = conn.execute("SELECT * FROM students")
    return cur.fetchall()


def run():
    conn = sqlite3.connect(":memory:")
    setup_db(conn)

    print("=== Student Registration ===")
    while True:
        try:
            name = input("Name (or 'done' to finish): ").strip()
        except EOFError:
            break
        if name.lower() == "done":
            break
        gender    = input("Gender (M/F): ").strip()
        email     = input("Email: ").strip()
        physics   = int(input("Physics marks: "))
        chemistry = int(input("Chemistry marks: "))
        maths     = int(input("Maths marks: "))
        add_student(conn, name, gender, email, physics, chemistry, maths)
        print("  Record added.\n")

    rows = list_students(conn)
    print(f"\n{'ID':<5} {'Name':<15} {'Gender':<8} {'Email':<25} {'Phy':<5} {'Chem':<5} {'Math'}")
    print("-" * 70)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<15} {row[2]:<8} {row[3]:<25} {row[4]:<5} {row[5]:<5} {row[6]}")
    conn.close()


if __name__ == "__main__":
    run()

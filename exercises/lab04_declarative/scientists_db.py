"""
Lab 04 – Declarative Programming
Program A: Create a table for scientists with ID, first name, last name,
gender, and date of birth; insert 5 rows and display them.
"""

import sqlite3


def create_scientists_table():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE scientists (
            id          INTEGER PRIMARY KEY,
            first_name  TEXT NOT NULL,
            last_name   TEXT NOT NULL,
            gender      TEXT NOT NULL,
            dob         TEXT NOT NULL
        )
    """)

    rows = [
        (1, "Albert", "Einstein",  "M", "1879-03-14"),
        (2, "Marie",  "Curie",     "F", "1867-11-07"),
        (3, "Isaac",  "Newton",    "M", "1643-01-04"),
        (4, "Nikola", "Tesla",     "M", "1856-07-10"),
        (5, "Ada",    "Lovelace",  "F", "1815-12-10"),
    ]
    cur.executemany("INSERT INTO scientists VALUES (?, ?, ?, ?, ?)", rows)
    conn.commit()

    cur.execute("SELECT * FROM scientists")
    fetched = cur.fetchall()

    print(f"{'ID':<5} {'First Name':<12} {'Last Name':<12} {'Gender':<8} {'Date of Birth'}")
    print("-" * 55)
    for row in fetched:
        print(f"{row[0]:<5} {row[1]:<12} {row[2]:<12} {row[3]:<8} {row[4]}")

    conn.close()
    return fetched


if __name__ == "__main__":
    create_scientists_table()

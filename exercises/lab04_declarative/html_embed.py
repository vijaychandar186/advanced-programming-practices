"""
Lab 04 – Declarative Programming
Program B: Python code embedded with HTML tags to generate a simple web page.
"""


def generate_html():
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob",   "age": 25},
        {"name": "Carol", "age": 28},
    ]

    rows = "\n".join(
        f"    <tr><td>{p['name']}</td><td>{p['age']}</td></tr>"
        for p in people
    )

    html = f"""<!DOCTYPE html>
<html>
<head><title>Person List</title></head>
<body>
  <h1>Person List</h1>
  <table border="1">
    <tr><th>Name</th><th>Age</th></tr>
{rows}
  </table>
</body>
</html>"""
    return html


if __name__ == "__main__":
    print(generate_html())

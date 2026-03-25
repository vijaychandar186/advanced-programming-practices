"""
Lab 11 – Logic Programming
Program C: Logic-based team hierarchy.
Alice and Franklin are Team Leaders under Project Head John.
Bob, Dawn, Trinity, and Christine are Team Members under Alice.
Find the number of staff directly reporting to Alice and John.
"""

REPORTS_TO: dict[str, list[str]] = {
    "John":     ["Alice", "Franklin"],
    "Alice":    ["Bob", "Dawn", "Trinity", "Christine"],
    "Franklin": [],
}


def direct_reports(person: str) -> list[str]:
    return REPORTS_TO.get(person, [])


def count_reports(person: str) -> int:
    return len(direct_reports(person))


def is_team_member(person: str) -> bool:
    for leader, members in REPORTS_TO.items():
        if person in members and not direct_reports(person):
            return True
    return False


if __name__ == "__main__":
    for person in ["John", "Alice", "Franklin", "Bob"]:
        reports = direct_reports(person)
        print(f"{person} → {count_reports(person)} direct report(s): {reports}")

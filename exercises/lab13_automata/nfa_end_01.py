"""
Lab 13 – Automata-Based Programming
Program C: NFA (simulated via subset construction) that recognises binary
strings ending with '01'.

States: q0 (start / anywhere in string)
        q1 (just saw '0')
        q2 (just saw '01'  — accepting)
"""


def nfa_ends_01(s: str) -> bool:
    transitions = {
        "q0": {"0": {"q0", "q1"}, "1": {"q0"}},
        "q1": {"0": {"q1"},       "1": {"q2"}},
        "q2": {"0": {"q1"},       "1": {"q0"}},
    }

    states = {"q0"}
    for ch in s:
        next_states: set[str] = set()
        for st in states:
            next_states |= transitions.get(st, {}).get(ch, set())
        states = next_states

    return "q2" in states


if __name__ == "__main__":
    tests = ["01", "101", "001", "0101", "10", "00", "1", "0", "11", "0011"]
    for t in tests:
        verdict = "ACCEPT" if nfa_ends_01(t) else "REJECT"
        print(f"  '{t}' → {verdict}")

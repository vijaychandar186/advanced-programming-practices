"""
Lab 13 – Automata-Based Programming
Program A: DFA that accepts binary strings starting with '1' and ending
with '0' over the alphabet {0, 1}.

States:
  start   – initial state
  valid_1 – read '1' at start; last char was '1'
  accept  – started with '1'; last char was '0'  (accepting)
  dead    – trap state (started with '0' or empty)
"""


def dfa_starts_1_ends_0(s: str) -> bool:
    if not s:
        return False

    state = "start"
    for ch in s:
        if state == "start":
            state = "valid_1" if ch == "1" else "dead"
        elif state == "valid_1":
            state = "accept" if ch == "0" else "valid_1"
        elif state == "accept":
            state = "accept" if ch == "0" else "valid_1"
        # dead stays dead

    return state == "accept"


if __name__ == "__main__":
    tests = ["10", "100", "110", "1010", "0", "01", "1", "11", "1110", ""]
    for t in tests:
        verdict = "ACCEPT" if dfa_starts_1_ends_0(t) else "REJECT"
        print(f"  '{t}' → {verdict}")

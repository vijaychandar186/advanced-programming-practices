"""
Lab 13 – Automata-Based Programming
Program B: NFA (simulated via subset construction) that matches strings
over {a, b} which begin with 'a', end with 'a', and contain no consecutive 'b's.

States: q0 (start), q1 (saw opening 'a'), q2 (in body, last was 'a'),
        q3 (in body, last was 'b'), q4 (dead – consecutive 'b')
"""


def nfa_a_no_consecutive_b(s: str) -> bool:
    """
    NFA subset-construction simulation.
    Transitions:
      q0 on 'a' → {q1}
      q0 on 'b' → {}             (must start with 'a')
      q1 on 'a' → {q1, q2}       (single char "a" is also accepted)
      q1 on 'b' → {q3}
      q2 on 'a' → {q2}
      q2 on 'b' → {q3}
      q3 on 'a' → {q2}
      q3 on 'b' → {q4}  (consecutive b)
      q4 on * → {q4}             (trap)
    Accept: {q1, q2}
    """
    transitions = {
        "q0": {"a": {"q1"},       "b": set()},
        "q1": {"a": {"q1", "q2"}, "b": {"q3"}},
        "q2": {"a": {"q2"},       "b": {"q3"}},
        "q3": {"a": {"q2"},       "b": {"q4"}},
        "q4": {"a": {"q4"},       "b": {"q4"}},
    }
    accept_states = {"q1", "q2"}

    states = {"q0"}
    for ch in s:
        next_states: set[str] = set()
        for st in states:
            next_states |= transitions.get(st, {}).get(ch, set())
        states = next_states

    return bool(states & accept_states)


if __name__ == "__main__":
    tests = ["a", "aba", "ababa", "aa", "abb", "ba", "b", "abba", "aab", "abab"]
    for t in tests:
        verdict = "ACCEPT" if nfa_a_no_consecutive_b(t) else "REJECT"
        print(f"  '{t}' → {verdict}")

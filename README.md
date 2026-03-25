# Advanced Programming Practices

Lab exercises covering 14 programming paradigms, implemented in Python.

## Structure

```
exercises/
├── lab01_procedural/       # Factorial, cube (def + lambda), string counting
├── lab02_structural/       # List merging, stats counter, greatest of three
├── lab03_oop/              # Turn-100 calculator, name reverser, day-of-week
├── lab04_declarative/      # SQLite scientists DB, HTML generation, student DB
├── lab05_imperative/       # Number pattern, top scores, tuition calculator
├── lab06_event_gui/        # Calculator GUI, greeter GUI, registration form
├── lab07_functional/       # map/filter/lambda — doubles, list ops, Fibonacci
├── lab08_parallel/         # Threading (target & run), multiprocessing.Process
├── lab09_concurrent/       # Race condition, Lock synchronisation, Semaphore
├── lab10_dependent_type/   # Union, Literal, @overload
├── lab11_logic/            # Regex matching, safe AST eval, team hierarchy
├── lab12_network/          # TCP chat, echo server, FTP file transfer
├── lab13_automata/         # DFA (binary strings), NFA (vowel), NFA (end-01)
└── lab14_symbolic/         # SymPy — algebra, derivatives, integrals
tests/
└── run_tests.py            # Automated test suite (49 checks)
```

## Running the tests

```bash
# Run all labs
python3 tests/run_tests.py

# Run a single lab
python3 tests/run_tests.py --lab 07
```

## Lab overview

| Lab | Paradigm | Programs |
|-----|----------|----------|
| 01 | Procedural | `factorial.py`, `cube.py`, `count_emma.py` |
| 02 | Structural | `odd_even_lists.py`, `stats_counter.py`, `greatest_of_three.py` |
| 03 | OOP | `turn_100.py`, `reverse_name.py`, `day_of_week.py` |
| 04 | Declarative | `scientists_db.py`, `html_embed.py`, `student_db.py` |
| 05 | Imperative | `number_pattern.py`, `top_scores.py`, `tuition_calculator.py` |
| 06 | Event-Driven / GUI | `calculator_gui.py`, `greeter_gui.py`, `registration_form.py` |
| 07 | Functional | `double_numbers.py`, `list_operations.py`, `fibonacci_filter.py` |
| 08 | Parallel | `thread_target.py`, `thread_run.py`, `process_method.py` |
| 09 | Concurrent | `race_condition.py`, `lock_sync.py`, `semaphore.py` |
| 10 | Dependent Type | `union_example.py`, `literal_example.py`, `overload_example.py` |
| 11 | Logic | `math_expression.py`, `eval_expression.py`, `team_hierarchy.py` |
| 12 | Network | `tcp_chat_server/client.py`, `echo_server/client.py`, `ftp_server/client.py` |
| 13 | Automata-Based | `dfa_binary.py`, `nfa_vowel.py`, `nfa_end_01.py` |
| 14 | Symbolic | `algebra.py`, `derivatives.py`, `integrals.py` |

## Notes

- **Lab 06 (GUI)** uses `tkinter`; falls back to CLI mode when no display is available. The underlying logic functions are directly importable and fully testable.
- **Lab 12 (Network)** programs bind to loopback ports 6000–6002. Start the server script first, then the client in a second terminal.
- **Lab 14 (Symbolic)** uses [SymPy](https://www.sympy.org/). Install with `pip install sympy`. Programs print expected results if SymPy is not installed.

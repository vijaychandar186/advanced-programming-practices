#!/usr/bin/env python3
"""
Automated test suite for Advanced Programming Practices lab implementations.

Tests each lab's Python programs by spawning subprocesses, piping stdin,
and asserting expected output.  Network labs (lab12) spawn server and
client processes and exchange data over the loopback interface.

Run:
    python3 tests/run_tests.py            # all labs
    python3 tests/run_tests.py --lab 01   # single lab
"""

import argparse
import os
import shutil
import socket
import subprocess
import sys
import threading
import time

# ── Paths ─────────────────────────────────────────────────────────────────────
ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY_LABS = os.path.join(ROOT, "exercises")

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"

results = []


# ── Helpers ───────────────────────────────────────────────────────────────────

def run_prog(path, stdin_data=b"", timeout=8):
    """Run a Python script, return (stdout_bytes, returncode)."""
    try:
        proc = subprocess.run(
            [sys.executable, path],
            input=stdin_data,
            capture_output=True,
            timeout=timeout,
        )
        return proc.stdout, proc.returncode
    except subprocess.TimeoutExpired:
        return b"", -1


def record(lab, name, passed, detail=""):
    tag  = PASS if passed else FAIL
    line = f"  [{tag}] Lab {lab}: {name}"
    if detail:
        line += f" — {detail}"
    print(line)
    results.append((lab, name, passed, detail))


def wait_for_port(host, port, timeout=5.0):
    """Block until a TCP port is in LISTEN state (non-consuming check)."""
    port_hex = format(port, "04X")
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with open("/proc/net/tcp") as f:
                for line in f:
                    parts = line.split()
                    if len(parts) >= 4 and parts[3] == "0A":
                        if parts[1].endswith(":" + port_hex):
                            return True
        except OSError:
            try:
                s = socket.create_connection((host, port), timeout=0.2)
                s.close()
                return True
            except OSError:
                pass
        time.sleep(0.05)
    return False


def communicate_pair(server, server_input, client, client_input, timeout=8):
    """Feed stdin to both processes and collect stdout concurrently."""
    for proc, data in ((server, server_input), (client, client_input)):
        if data and proc.stdin:
            try:
                proc.stdin.write(data)
                proc.stdin.flush()
                proc.stdin.close()
            except BrokenPipeError:
                pass
            proc.stdin = None

    out = {}

    def run(key, proc):
        try:
            stdout, _ = proc.communicate(timeout=timeout)
            out[key] = stdout
        except subprocess.TimeoutExpired:
            proc.kill()
            try:
                out[key] = proc.communicate()[0]
            except Exception:
                out[key] = b""

    t1 = threading.Thread(target=run, args=("server", server))
    t2 = threading.Thread(target=run, args=("client", client))
    t1.start(); t2.start()
    t1.join(timeout + 3); t2.join(timeout + 3)
    return out.get("server", b""), out.get("client", b"")


def kill_proc(proc):
    try:
        proc.kill()
        proc.communicate()
    except Exception:
        pass


def popen(path, cwd=None):
    return subprocess.Popen(
        [sys.executable, path],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        cwd=cwd,
    )


# ── Lab 01: Procedural ────────────────────────────────────────────────────────

def test_lab01():
    lab  = "01"
    base = os.path.join(PY_LABS, "lab01_procedural")

    out, _ = run_prog(os.path.join(base, "factorial.py"), b"5\n")
    record(lab, "factorial(5) == 120", b"120" in out,
           out.decode(errors="replace").strip())

    out, _ = run_prog(os.path.join(base, "cube.py"), b"3\n")
    record(lab, "cube(3) == 27", b"27" in out,
           out.decode(errors="replace").strip())

    out, _ = run_prog(os.path.join(base, "count_emma.py"),
                      b"Emma is here, Emma is there\n")
    record(lab, "count_emma: 2 occurrences", b"2" in out,
           out.decode(errors="replace").strip())


# ── Lab 02: Structural ────────────────────────────────────────────────────────

def test_lab02():
    lab  = "02"
    base = os.path.join(PY_LABS, "lab02_structural")

    out, _ = run_prog(os.path.join(base, "odd_even_lists.py"),
                      b"1 2 3 4 5\n2 4 6 8\n")
    record(lab, "odd_even_lists: odd from list1, even from list2",
           b"1" in out and b"3" in out and b"4" in out,
           out.decode(errors="replace").strip())

    out, _ = run_prog(os.path.join(base, "stats_counter.py"),
                      b"3\n-2\n4\n-1\n0\n")
    record(lab, "stats_counter: positives=2 negatives=2",
           b"Positives: 2" in out and b"Negatives: 2" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "greatest_of_three.py"), b"3\n7\n5\n")
    record(lab, "greatest_of_three(3,7,5) == 7", b"7" in out,
           out.decode(errors="replace").strip())


# ── Lab 03: OOP ───────────────────────────────────────────────────────────────

def test_lab03():
    lab  = "03"
    base = os.path.join(PY_LABS, "lab03_oop")

    out, _ = run_prog(os.path.join(base, "turn_100.py"), b"Alice\n20\n")
    record(lab, "turn_100: year in 21xx", b"21" in out,
           out.decode(errors="replace").strip())

    out, _ = run_prog(os.path.join(base, "reverse_name.py"), b"John\nDoe\n")
    record(lab, "reverse_name: 'Doe John'", b"Doe John" in out,
           out.decode(errors="replace").strip())

    out, _ = run_prog(os.path.join(base, "day_of_week.py"), b"1\n2\n")
    record(lab, "day_of_week: Monday+2 = Wednesday", b"Wednesday" in out,
           out.decode(errors="replace").strip())


# ── Lab 04: Declarative ───────────────────────────────────────────────────────

def test_lab04():
    lab  = "04"
    base = os.path.join(PY_LABS, "lab04_declarative")

    out, _ = run_prog(os.path.join(base, "scientists_db.py"))
    record(lab, "scientists_db: Einstein & Curie present",
           b"Einstein" in out and b"Curie" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "html_embed.py"))
    record(lab, "html_embed: valid HTML with table",
           b"<html>" in out and b"<table" in out and b"Alice" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "student_db.py"),
                      b"Alice\nF\nalice@example.com\n90\n85\n92\ndone\n")
    record(lab, "student_db: record inserted", b"Alice" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])


# ── Lab 05: Imperative ────────────────────────────────────────────────────────

def test_lab05():
    lab  = "05"
    base = os.path.join(PY_LABS, "lab05_imperative")

    out, _ = run_prog(os.path.join(base, "number_pattern.py"), b"5\n")
    record(lab, "number_pattern: row 5 = '5 5 5 5 5'",
           b"5 5 5 5 5" in out,
           out.decode(errors="replace").replace("\n", "|").strip()[:80])

    out, _ = run_prog(os.path.join(base, "top_scores.py"), b"3\n90\n85\n92\n")
    record(lab, "top_scores: highest=92 second=90",
           b"92" in out and b"90" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "tuition_calculator.py"))
    record(lab, "tuition_calculator: $16,288.46 in year 10",
           b"16,288" in out or b"16288" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])


# ── Lab 06: Event-Driven / GUI ────────────────────────────────────────────────

def test_lab06():
    lab  = "06"
    base = os.path.join(PY_LABS, "lab06_event_gui")
    sys.path.insert(0, base)

    try:
        import calculator_gui
        res = calculator_gui.calculate("2 + 3")
        record(lab, "calculator_gui: 2+3 = '5'", res == "5", f"got={res!r}")

        res2 = calculator_gui.calculate("6 * 7")
        record(lab, "calculator_gui: 6*7 = '42'", res2 == "42", f"got={res2!r}")

        import greeter_gui
        msg = greeter_gui.greet("Alice")
        record(lab, "greeter_gui: greet Alice", "Alice" in msg, msg)

        import registration_form, sqlite3
        conn = sqlite3.connect(":memory:")
        registration_form.setup_db(conn)
        registration_form.add_record(conn, "Bob", "b@x.com", "M", 80, 75, 90)
        rows = registration_form.view_records(conn)
        record(lab, "registration_form: DB round-trip",
               len(rows) == 1 and rows[0][1] == "Bob")
        conn.close()

    except Exception as e:
        record(lab, "GUI module logic", False, str(e))
    finally:
        sys.path.pop(0)
        for mod in ["calculator_gui", "greeter_gui", "registration_form"]:
            sys.modules.pop(mod, None)


# ── Lab 07: Functional ────────────────────────────────────────────────────────

def test_lab07():
    lab  = "07"
    base = os.path.join(PY_LABS, "lab07_functional")

    out, _ = run_prog(os.path.join(base, "double_numbers.py"))
    record(lab, "double_numbers: quadrupled [8,16,24,32]",
           b"8" in out and b"16" in out and b"32" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "list_operations.py"))
    record(lab, "list_operations: product contains 20 and 120",
           b"20" in out and b"120" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "fibonacci_filter.py"))
    record(lab, "fibonacci_filter: odds and evens separated",
           b"1, 1, 3, 5" in out and b"0, 2, 8" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])


# ── Lab 08: Parallel ─────────────────────────────────────────────────────────

def test_lab08():
    lab  = "08"
    base = os.path.join(PY_LABS, "lab08_parallel")

    out, _ = run_prog(os.path.join(base, "thread_target.py"), timeout=10)
    record(lab, "thread_target: completes", b"All threads completed." in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "thread_run.py"), timeout=10)
    record(lab, "thread_run: completes", b"All threads completed." in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "process_method.py"), timeout=15)
    record(lab, "process_method: completes", b"All processes completed." in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])


# ── Lab 09: Concurrent ────────────────────────────────────────────────────────

def test_lab09():
    lab  = "09"
    base = os.path.join(PY_LABS, "lab09_concurrent")

    out, _ = run_prog(os.path.join(base, "race_condition.py"), timeout=15)
    record(lab, "race_condition: runs to completion",
           b"Expected: 500000" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "lock_sync.py"), timeout=15)
    record(lab, "lock_sync: counter correct", b"PASSED" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "semaphore.py"), timeout=10)
    record(lab, "semaphore: demo completes", b"Semaphore demo complete." in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])


# ── Lab 10: Dependent Type ────────────────────────────────────────────────────

def test_lab10():
    lab  = "10"
    base = os.path.join(PY_LABS, "lab10_dependent_type")

    out, _ = run_prog(os.path.join(base, "union_example.py"))
    record(lab, "union_example: Integer 42", b"Integer: 42" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "literal_example.py"))
    record(lab, "literal_example: move north 5 steps",
           b"Moving 5 step(s) north." in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "overload_example.py"))
    record(lab, "overload_example: int→str dispatch",
           b"Got integer: 42" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])


# ── Lab 11: Logic ─────────────────────────────────────────────────────────────

def test_lab11():
    lab  = "11"
    base = os.path.join(PY_LABS, "lab11_logic")

    out, _ = run_prog(os.path.join(base, "math_expression.py"))
    record(lab, "math_expression: '3 + 4' → addition",
           b"addition" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "eval_expression.py"))
    record(lab, "eval_expression: '3+4*2 = 11'", b"11" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "team_hierarchy.py"))
    record(lab, "team_hierarchy: Alice has 4 reports", b"4" in out,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])


# ── Lab 12: Network ───────────────────────────────────────────────────────────

def test_lab12():
    lab  = "12"
    base = os.path.join(PY_LABS, "lab12_network")

    # TCP Chat
    server = popen(os.path.join(base, "tcp_chat_server.py"))
    if not wait_for_port("127.0.0.1", 6000):
        record(lab, "TCP chat server starts", False, "port 6000 not open")
        kill_proc(server)
    else:
        record(lab, "TCP chat server starts", True)
        client = popen(os.path.join(base, "tcp_chat_client.py"))
        time.sleep(0.5)
        server_out, client_out = communicate_pair(
            server, b"Hi from server\n",
            client, b"hello server\nquit\n",
        )
        record(lab, "TCP chat: server receives client msg",
               b"hello server" in server_out,
               server_out.decode(errors="replace").replace("\n", " ").strip()[:80])
        record(lab, "TCP chat: client receives server reply",
               b"Hi from server" in client_out,
               client_out.decode(errors="replace").replace("\n", " ").strip()[:80])

    time.sleep(0.3)

    # Echo
    server = popen(os.path.join(base, "echo_server.py"))
    if not wait_for_port("127.0.0.1", 6001):
        record(lab, "Echo server starts", False, "port 6001 not open")
        kill_proc(server)
    else:
        record(lab, "Echo server starts", True)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect(("127.0.0.1", 6001))
            test_msg = b"hello echo"
            s.sendall(test_msg)
            data = s.recv(1024)
            record(lab, "Echo: message echoed back", data == test_msg,
                   f"sent={test_msg!r} got={data!r}")
            s.sendall(b"quit")
            s.recv(1024)
        except socket.timeout:
            record(lab, "Echo", False, "timeout")
        finally:
            s.close()
            kill_proc(server)

    time.sleep(0.3)

    # FTP
    client_files = os.path.join(base, "client_files")
    if os.path.exists(client_files):
        shutil.rmtree(client_files)

    server = popen(os.path.join(base, "ftp_server.py"), cwd=base)
    if not wait_for_port("127.0.0.1", 6002):
        record(lab, "FTP server starts", False, "port 6002 not open")
        kill_proc(server)
    else:
        record(lab, "FTP server starts", True)
        client = popen(os.path.join(base, "ftp_client.py"), cwd=base)
        time.sleep(0.5)
        try:
            client_out, _ = client.communicate(
                input=b"list\ndownload sample.txt\nquit\n", timeout=12)
            server.wait(timeout=3)
        except subprocess.TimeoutExpired:
            record(lab, "FTP operations", False, "timeout")
            kill_proc(server); kill_proc(client)
            return

        record(lab, "FTP LIST: sample.txt listed", b"sample.txt" in client_out,
               client_out.decode(errors="replace").replace("\n", " ").strip()[:80])

        downloaded = os.path.join(client_files, "sample.txt")
        record(lab, "FTP DOWNLOAD: file saved", os.path.isfile(downloaded))

        if os.path.isfile(downloaded):
            with open(downloaded) as f:
                content = f.read()
            record(lab, "FTP DOWNLOAD: content correct",
                   "Lab 12" in content or "sample" in content.lower())


# ── Lab 13: Automata ─────────────────────────────────────────────────────────

def test_lab13():
    lab  = "13"
    base = os.path.join(PY_LABS, "lab13_automata")

    out, _ = run_prog(os.path.join(base, "dfa_binary.py"))
    text = out.decode(errors="replace")
    record(lab, "DFA binary: '10' ACCEPT, '0' REJECT",
           "'10' \u2192 ACCEPT" in text and "'0' \u2192 REJECT" in text,
           text.replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "nfa_vowel.py"))
    text = out.decode(errors="replace")
    record(lab, "NFA vowel: 'aba' ACCEPT, 'abb' REJECT",
           "'aba' \u2192 ACCEPT" in text and "'abb' \u2192 REJECT" in text,
           text.replace("\n", " ").strip()[:80])

    out, _ = run_prog(os.path.join(base, "nfa_end_01.py"))
    text = out.decode(errors="replace")
    record(lab, "NFA end_01: '01' ACCEPT, '10' REJECT",
           "'01' \u2192 ACCEPT" in text and "'10' \u2192 REJECT" in text,
           text.replace("\n", " ").strip()[:80])


# ── Lab 14: Symbolic ─────────────────────────────────────────────────────────

def test_lab14():
    lab  = "14"
    base = os.path.join(PY_LABS, "lab14_symbolic")

    out, rc = run_prog(os.path.join(base, "algebra.py"), timeout=20)
    record(lab, "algebra.py: runs without error", rc == 0,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, rc = run_prog(os.path.join(base, "derivatives.py"), timeout=20)
    record(lab, "derivatives.py: runs without error", rc == 0,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])

    out, rc = run_prog(os.path.join(base, "integrals.py"), timeout=20)
    record(lab, "integrals.py: runs without error", rc == 0,
           out.decode(errors="replace").replace("\n", " ").strip()[:80])


# ── Summary ───────────────────────────────────────────────────────────────────

def print_summary():
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    passed = sum(1 for _, _, ok, _ in results if ok)
    failed = sum(1 for _, _, ok, _ in results if not ok)
    total  = len(results)
    print(f"  Total : {total}")
    print(f"  Passed: {passed}  ({PASS})")
    print(f"  Failed: {failed}  ({FAIL})")
    if failed:
        print("\nFailed tests:")
        for lab, name, ok, detail in results:
            if not ok:
                print(f"  Lab {lab}: {name}  — {detail}")
    print("=" * 60)
    return failed == 0


# ── Entry Point ───────────────────────────────────────────────────────────────

LAB_TESTS = {
    "01": test_lab01,
    "02": test_lab02,
    "03": test_lab03,
    "04": test_lab04,
    "05": test_lab05,
    "06": test_lab06,
    "07": test_lab07,
    "08": test_lab08,
    "09": test_lab09,
    "10": test_lab10,
    "11": test_lab11,
    "12": test_lab12,
    "13": test_lab13,
    "14": test_lab14,
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="APP Lab Test Runner")
    parser.add_argument("--lab", help="Run only a specific lab (e.g. 03)")
    args = parser.parse_args()

    print("Advanced Programming Practices — Test Suite")
    print("=" * 60)

    labs_to_run = [args.lab] if args.lab else sorted(LAB_TESTS)

    for lab_id in labs_to_run:
        if lab_id not in LAB_TESTS:
            print(f"  [SKIP] Lab {lab_id}: no automated test")
            continue
        print(f"\nLab {lab_id}:")
        try:
            LAB_TESTS[lab_id]()
        except Exception as e:
            record(lab_id, "test runner", False, str(e))
        time.sleep(0.2)

    ok = print_summary()
    sys.exit(0 if ok else 1)

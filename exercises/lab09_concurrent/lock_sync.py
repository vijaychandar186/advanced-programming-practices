"""
Lab 09 – Concurrent Programming
Program B: Synchronize threads using threading.Lock.
"""

import threading

counter = 0
lock = threading.Lock()
INCREMENTS = 100_000
THREADS = 5


def safe_increment():
    global counter
    for _ in range(INCREMENTS):
        with lock:
            counter += 1


if __name__ == "__main__":
    counter = 0
    threads = [threading.Thread(target=safe_increment) for _ in range(THREADS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    expected = INCREMENTS * THREADS
    print(f"Expected: {expected}")
    print(f"Got:      {counter}")
    print("Lock synchronization: " + ("PASSED" if counter == expected else "FAILED"))

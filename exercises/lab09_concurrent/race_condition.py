"""
Lab 09 – Concurrent Programming
Program A: Demonstrate a race condition using threads.
"""

import threading

counter = 0
INCREMENTS = 100_000
THREADS = 5


def increment():
    global counter
    for _ in range(INCREMENTS):
        tmp = counter
        counter = tmp + 1


if __name__ == "__main__":
    counter = 0
    threads = [threading.Thread(target=increment) for _ in range(THREADS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    expected = INCREMENTS * THREADS
    print(f"Expected: {expected}")
    print(f"Got:      {counter}")
    if counter != expected:
        print("Race condition detected! Counter is inconsistent.")
    else:
        print("No race condition detected this run (result may vary).")

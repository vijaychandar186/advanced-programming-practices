"""
Lab 08 – Parallel Programming
Program A: Threading using the target method.
"""

import threading
import time


def worker(name, delay):
    time.sleep(delay)
    print(f"[Thread] '{name}' running (delay={delay:.1f}s)")


if __name__ == "__main__":
    threads = [
        threading.Thread(target=worker, args=(f"Worker-{i}", 0.05 * i))
        for i in range(1, 4)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("All threads completed.")

"""
Lab 08 – Parallel Programming
Program B: Threading using the run() method (subclassing Thread).
"""

import threading
import time


class WorkerThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.worker_name = name
        self.delay = delay

    def run(self):
        time.sleep(self.delay)
        print(f"[Thread] '{self.worker_name}' running (delay={self.delay:.1f}s)")


if __name__ == "__main__":
    threads = [WorkerThread(f"Worker-{i}", 0.05 * i) for i in range(1, 4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("All threads completed.")

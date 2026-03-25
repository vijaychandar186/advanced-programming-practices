"""
Lab 08 – Parallel Programming
Program C: Parallelism using multiprocessing.Process.
"""

import multiprocessing
import time


def worker(name, delay):
    time.sleep(delay)
    print(f"[Process] '{name}' PID={multiprocessing.current_process().pid}")


if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=worker, args=(f"Worker-{i}", 0.05 * i))
        for i in range(1, 4)
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print("All processes completed.")

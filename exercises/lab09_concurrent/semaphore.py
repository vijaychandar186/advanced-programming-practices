"""
Lab 09 – Concurrent Programming
Program C: Implement a Semaphore to control access to a shared resource.
"""

import threading
import time

semaphore = threading.Semaphore(2)   # at most 2 threads at once
log = []
log_lock = threading.Lock()


def access_resource(name):
    with log_lock:
        log.append(f"{name}: waiting")
    with semaphore:
        with log_lock:
            log.append(f"{name}: acquired")
        time.sleep(0.05)
        with log_lock:
            log.append(f"{name}: released")


if __name__ == "__main__":
    threads = [
        threading.Thread(target=access_resource, args=(f"Thread-{i}",))
        for i in range(1, 6)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    for entry in log:
        print(entry)
    print("Semaphore demo complete.")

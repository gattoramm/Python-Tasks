import threading
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print(f"I am Worker {number}, I slept for {sleep} seconds")


if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
    print("All Threads are queued, let's see when they finish!")

from threading import Lock, current_thread, Thread
from time import time, sleep


class TokenBucket:
    def __init__(self, capacity):
        self.capacity = capacity
        self.tokens = 0
        self.last_access = time()
        self.lock = Lock()

    def get(self):
        with self.lock:
            self.tokens += int(time() - self.last_access)

            if self.tokens > self.capacity:
                self.tokens = self.capacity

            if self.tokens == 0:
                sleep(1)
            else:
                self.tokens -= 1
            self.last_access = time()

            print("Granting {0} token at {1} ".format(current_thread().getName(), self.last_access))

tBucket = TokenBucket(2)
threads = []
for i in range(10):
    threads.append(Thread(target=tBucket.get(), name=f't{i}'))

for thread in threads:
    thread.start()
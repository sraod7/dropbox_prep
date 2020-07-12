import time
from threading import Condition, Thread, current_thread, Lock


class BlockingQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.cond = Condition()
        self.current_size = 0

    def add(self, element):
        self.cond.acquire()
        while self.current_size == self.capacity:
            print(f'Producer {current_thread().name} is blocked')
            self.cond.wait()

        self.queue.append(element)
        self.current_size += 1

        self.cond.notifyAll()
        self.cond.release()

    def remove(self):
        self.cond.acquire()
        while self.current_size == 0:
            print(f'Consumer {current_thread().name} is blocked')
            self.cond.wait()

        element = self.queue.pop(0)
        self.current_size -= 1
        self.cond.notifyAll()
        self.cond.release()

        return element


class NonBlockingQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.curr_size = 0
        self.lock = Lock()

    def add(self, item):
        with self.lock:
            if self.curr_size == self.capacity:
                return False
            self.queue.append(item)
            self.curr_size += 1
            return True


    def remove(self):
        with self.lock:
            if self.curr_size == 0:
                return False
            item = self.queue.pop(0)
            self.curr_size -= 1

            return item

def consumer(q):
    while True:
        print(f'Consumer {current_thread().name}: {q.remove()}')
        time.sleep(2)

def producer(q, item):
    while True:
        q.add(item)
        item += 1
        time.sleep(1)


queue = NonBlockingQueue(5)
c1 = Thread(target=consumer, name='c1', args=(queue,))
c2 = Thread(target=consumer, name='c2', args=(queue,))
p1 = Thread(target=producer, name='p1', args=(queue, 1))
p2 = Thread(target=producer, name='p2', args=(queue, 1000))


c1.start()
p1.start()
c2.start()
p2.start()

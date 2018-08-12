from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        return self._data.popleft()

    def max(self):
        return max(self._data)

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')

    queue.dequeue()

    assert queue.max() == 'b'

from enum import Enum


class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, x):
        if self._is_empty() or len(self.enqueue_stack) > 0:
            self.enqueue_stack.append(x)
        elif len(self.dequeue_stack) > 0:
            self._move(self.dequeue_stack, self.enqueue_stack)
            self.enqueue_stack.append(x)

    def dequeue(self):
        if len(self.dequeue_stack) > 0:
            return self.dequeue_stack.pop()
        elif len(self.enqueue_stack) > 0:
            self._move(self.enqueue_stack, self.dequeue_stack)
            return self.dequeue_stack.pop()

    def _is_empty(self):
        return len(self.enqueue_stack) == len(self.dequeue_stack) == 0

    @staticmethod
    def _move(x, y):
        while len(x) > 0:
            y.append(x.pop())

    def to_list(self):
        if len(self.enqueue_stack) > 0:
            return [x for x in self.enqueue_stack]

        if len(self.dequeue_stack) > 0:
            return [x for x in reversed(self.dequeue_stack)]


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    print(queue.to_list())

    queue.dequeue()
    print(queue.to_list())

    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    print(queue.to_list())

    queue.dequeue()
    print(queue.to_list())

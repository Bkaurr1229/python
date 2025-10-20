from collections import deque

class Queue:
    def __init__(self):
        self._queue = deque()

    def enqueue(self, item):
        """Add an element to the end of the queue."""
        self._queue.append(item)

    def dequeue(self):
        """Remove and return the element at the front of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._queue.popleft()

    def peek(self):
        """Return the element at the front of the queue without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self._queue) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return len(self._queue)

q = Queue()
q.enqueue(11)
q.peek()
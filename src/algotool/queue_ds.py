from collections import deque

from .errors import QueueEmptyError


class Queue:
    def __init__(self, iterable=None):
        self._data = deque(iterable) if iterable is not None else deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if not self._data:
            raise QueueEmptyError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        if not self._data:
            raise QueueEmptyError("peek from empty queue")
        return self._data[0]

    def __len__(self):
        return len(self._data)

    def __bool__(self):
        return bool(self._data)

    def __iter__(self):
        return iter(tuple(self._data))

    def __repr__(self):
        return f"Queue({list(self._data)!r})"
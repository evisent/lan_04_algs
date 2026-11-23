import pytest

from algotool.errors import QueueEmptyError
from algotool.queue_ds import Queue


def test_fifo():
    q = Queue()
    for x in (1, 2, 3):
        q.enqueue(x)
    assert [q.dequeue(), q.dequeue(), q.dequeue()] == [1, 2, 3]


def test_peek():
    q = Queue([10, 20])
    assert q.peek() == 10
    assert len(q) == 2


def test_len_bool():
    q = Queue()
    assert not q
    assert len(q) == 0
    q.enqueue(1)
    assert q
    assert len(q) == 1


def test_empty_dequeue():
    with pytest.raises(QueueEmptyError):
        Queue().dequeue()


def test_empty_peek():
    with pytest.raises(QueueEmptyError):
        Queue().peek()


def test_empty_is_index_error():
    with pytest.raises(IndexError):
        Queue().peek()


def test_duplicates_negatives():
    q = Queue([-1, -1, 0, 0, 5, 5])
    out = [q.dequeue() for _ in range(len(q))]
    assert out == [-1, -1, 0, 0, 5, 5]
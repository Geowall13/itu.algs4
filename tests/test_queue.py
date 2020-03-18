import pytest
import random

from itu.algs4.fundamentals.queue import Queue
from itu.algs4.errors.errors import NoSuchElementException

@pytest.fixture
def q():
    return Queue()

def test_enqueue_dequeue(q):
    assert q.size() == 0
    q.enqueue(1)
    q.enqueue(0)
    q.enqueue(-1)
    q.enqueue(2147483648)
    assert q.size() == 4
    q.enqueue("Hello World")
    q.enqueue("")
    q.enqueue(None)
    assert q.size() == 7

    assert q.dequeue() == 1
    assert q.dequeue() == 0
    assert q.dequeue() == -1
    assert q.dequeue() == 2147483648
    assert q.dequeue() == "Hello World"
    assert q.dequeue() == ""
    assert q.dequeue() == None
    
    with pytest.raises(NoSuchElementException):
        q.dequeue()

def test_is_empty(q):
    assert q.is_empty()
    q.enqueue(0)
    q.enqueue(1)
    assert not q.is_empty()
    q.dequeue()
    q.dequeue()
    assert q.is_empty()

def test_size_len(q):
    for i in range(1000):
        assert q.size() == i
        assert len(q) == i # Currently just calls size()
        q.enqueue(i)
        
    for i in range(1000):
        assert q.size() == 1000 - i
        assert len(q) == 1000 - i # Currently just calls size()
        q.dequeue()

def test_peek(q):
    with pytest.raises(NoSuchElementException):
        q.peek()

    q.enqueue(1)
    assert q.peek() == 1
    q.enqueue(0)
    q.enqueue(-1)
    q.enqueue(2147483648)
    q.enqueue("Hello World")
    q.enqueue("")
    q.enqueue(None)

    assert q.peek() == 1
    q.dequeue()
    assert q.peek() == 0
    q.dequeue()
    assert q.peek() == -1
    q.dequeue()
    assert q.peek() == 2147483648
    q.dequeue()
    assert q.peek() == "Hello World"
    q.dequeue()
    assert q.peek() == ""
    q.dequeue()
    assert q.peek() == None
    q.dequeue()
    
    with pytest.raises(NoSuchElementException):
        q.peek()

def test_iter(q):
    for i in range(1000):
        q.enqueue(i)
    for i in q:
        assert q.dequeue() == i

def tests_repr(q):
    assert str(q) == ""
    q.enqueue(1)
    q.enqueue(0)
    q.enqueue(-1)
    q.enqueue(2147483648)
    q.enqueue("Hello World")
    q.enqueue("")
    q.enqueue(None)
    assert str(q) == "1 0 -1 2147483648 Hello World  None "
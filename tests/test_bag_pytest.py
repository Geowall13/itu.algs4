import pytest

from itu.algs4.fundamentals.bag import Bag

@pytest.fixture
def b():
    return Bag()

def test_add(b):
    b.add(-1)
    b.add(2147483648)
    b.add(0)
    assert(b.size() == 3)

def test_is_empty(b):
    assert(b.is_empty())
    b.add(1)
    assert(not b.is_empty())

def test_size_and_len(b):
    for i in range(100):
        assert(b.size() == i)
        assert(len(b) == i) # Currently just calls size()
        b.add(i)

def test_iter(b):
    for i in range(10):
        b.add(i)
    l = []
    for i in iter(b):
        l.append(i)
    for i in range(10):
        assert(i in l)
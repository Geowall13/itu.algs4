import pytest

from itu.algs4.fundamentals.binary_search import index_of

def test_index_of():
    a = [0,1,2,3,4,5,6,7,8,9]
    b = [0,0,1,1,2,2,3,3,4,4]
    c = [1]
    d = []

    assert index_of(a, 4) == 4
    assert index_of(a, 10) == -1
    assert index_of(a, -1) == -1
    assert index_of(b, 0) == 0 or 1
    assert index_of(b, -20) == -1
    assert index_of(c, 1) == 0
    assert index_of(c, 0) == -1
    assert index_of(d, 0), -1

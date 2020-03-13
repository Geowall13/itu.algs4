import pytest

from itu.algs4.fundamentals.binary_search import index_of

def test_index_of_no_dups():

    for i in range(1, 1000):
        l = []
        for j in range(i):
            l.append(j)

        assert index_of(l, 0) == 0
        assert index_of(l, -1) == -1

        k = len(l)
        assert index_of(l, (k//2)) == (k//2)
        assert index_of(l, k) == -1

def test_index_of_dups():

    for i in range(2, 1000):
        l = []
        for j in range(i):
            l.append(j//2)

        io0 = index_of(l, 0)
        assert io0 == 0 or io0 == 1
        assert index_of(l, -1) == -1

        # Helper values for next assert statements
        k = len(l)
        maxVal = l[k-1]
        ioHalf = index_of(l, maxVal//2)
        maxIndex = maxVal + (k % 2)
        
        assert ioHalf == maxIndex or ioHalf == maxIndex - 1
        assert index_of(l, (ceildiv(k, 2))) == -1

def test_index_of_handmade():

    a = [0,1,2,3,4,5,6,7,8,9]
    b = [0,0,1,1,2,2,3,3,4,4]
    c = [1]
    d = []

    assert index_of(a, 4) == 4
    assert index_of(a, 10) == -1
    assert index_of(a, -1) == -1
    assert index_of(b, 0) == 0 or index_of(b, 0) == 1
    assert index_of(b, -20) == -1
    assert index_of(c, 1) == 0
    assert index_of(c, 0) == -1
    assert index_of(d, 0), -1

# Division with ceiling instead of floor, to help with duplicate testing
def ceildiv(a, b):
    return -(-a // b)
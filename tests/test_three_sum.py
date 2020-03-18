import pytest

from itu.algs4.fundamentals.three_sum import ThreeSum
from itu.algs4.fundamentals.three_sum_fast import ThreeSumFast

def test_slow_count():
    assert ThreeSum.count([]) == 0
    assert ThreeSum.count([-1,0,1]) == 1
    assert ThreeSum.count([-1,0,2]) == 0
    assert ThreeSum.count([-2,2,0,-1,1]) == 2

    l = list(range(-5,6))
    assert ThreeSum.count(l) == 13

def test_fast_count():
    assert ThreeSumFast.count([]) == 0
    assert ThreeSumFast.count([-1,0,1]) == 1
    assert ThreeSumFast.count([-1,0,2]) == 0
    assert ThreeSumFast.count([-2,2,0,-1,1]) == 2

    l = list(range(-5,6))
    assert ThreeSumFast.count(l) == 13
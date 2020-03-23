import pytest

from itu.algs4.fundamentals.two_sum_fast import TwoSumFast

def test_count():
    assert TwoSumFast.count([]) == 0
    assert TwoSumFast.count([-1,1]) == 1
    assert TwoSumFast.count([-1,0,2]) == 0
    assert TwoSumFast.count([-2,2,0,-1,1]) == 2

    l = list(range(-5,6))
    assert TwoSumFast.count(l) == 5
import pytest

from itu.algs4.fundamentals.uf import UF, QuickUnionUF, WeightedQuickUnionUF, QuickFindUF


def test_initial_count():
    for i in range(100):
        assert UF(i).count() == i
        assert QuickUnionUF(i).count() == i
        assert WeightedQuickUnionUF(i).count() == i
        assert QuickFindUF(i).count() == i

@pytest.mark.parametrize(
    "uf",
    [
        UF(100),
        QuickUnionUF(100),
        QuickFindUF(100),
        WeightedQuickUnionUF(100)
    ]
)
def test_initial_connected(uf):
    for i in range(99):
        for j in range(i+1,99-i):
            assert not uf.connected(i,j)

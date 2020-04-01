import pytest


from itu.algs4.fundamentals.uf import UF, QuickUnionUF, WeightedQuickUnionUF, QuickFindUF

def test_count():
    for i in range(100):
        uf = UF(i)
        assert uf.count() == i

        quuf = QuickUnionUF(i)
        assert quuf.count() == i

        wquuf = WeightedQuickUnionUF(i)
        assert wquuf.count() == i

        qfuf = QuickFindUF(i)
        assert qfuf.count() == i

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
    for i in range(100):
        for j in range(i+1, 100-i):
            assert not uf.connected(i,j)

@pytest.mark.parametrize(
    "uf",
    [
        UF(100),
        QuickUnionUF(100),
        QuickFindUF(100),
        WeightedQuickUnionUF(100)
    ]
)
def test_union(uf):
    for i in range(1, 100):
        uf.union(0, i)
        assert uf.connected(i, i-1)
        assert uf.count() == 100-i


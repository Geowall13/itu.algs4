import random
import unittest

from itu.algs4.errors.errors import NoSuchElementException
from itu.algs4.searching.bst import BST


class TestBSTMethods(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_empty(self):
        self.assertTrue(self.bst.is_empty())
        self.bst.put(0, 0)
        self.assertFalse(self.bst.is_empty())

    def test_size(self):
        for i in range(10):
            self.assertEqual(i, self.bst.size())
            self.bst.put(str(i), i)

        for i in range(10):
            self.assertEqual(10, self.bst.size())
            self.bst.put(str(i), i + 1)  # key already there: no change in size

        for i in reversed(range(10)):
            self.assertEqual(i + 1, self.bst.size())
            self.bst.delete(str(i))

        self.assertEqual(0, self.bst.size())

    def test_floor_and_ceiling(self):
        self.bst.put(0, 0)
        self.bst.put(2, 2)
        self.assertEqual(0, self.bst.floor(0))
        self.assertEqual(0, self.bst.floor(1))
        self.assertEqual(2, self.bst.floor(2))
        self.assertEqual(2, self.bst.floor(3))
        self.assertEqual(0, self.bst.ceiling(-1))
        self.assertEqual(0, self.bst.ceiling(0))
        self.assertEqual(2, self.bst.ceiling(1))
        self.assertEqual(2, self.bst.ceiling(2))

    def test_rank_select(self):
        for i in range(0, 2 ** 8 + 2, 2):
            self.bst.put(i, i)
            self.assertEqual(0, self.bst.min())
            self.assertEqual(i, self.bst.max())
            self.assertEqual(i, self.bst.select(i // 2))
            self.assertEqual(i // 2, self.bst.rank(i))

    def test_exceptions(self):
        with self.assertRaises(NoSuchElementException):
            self.bst.min()
        with self.assertRaises(NoSuchElementException):
            self.bst.max()
        with self.assertRaises(NoSuchElementException):
            self.bst.floor(0)
        self.bst.put(0, 0)
        with self.assertRaises(NoSuchElementException):
            self.bst.floor(-1)


class LargerBSTMethods(unittest.TestCase):
    L = [1, 3, 6, 7, 10, 13, 16]

    def setUp(self):
        self.bst = BST()
        for x in self.L:
            self.bst.put(x, x)

    def test_put_and_get(self):
        st = self.bst
        for x in st.keys():
            self.assertEqual(st.get(x), x)
        for x in st.keys():
            st.put(x, st.get(x) - 1)
        for x in st.keys():
            self.assertEqual(st.get(x), x - 1)
        self.assertIsNone(st.get(2))
        st.put(2, 2)
        self.assertEqual(2, st.get(2))

    def test_keys(self):
        i = 0
        for x in self.bst.keys():
            self.assertEqual(x, self.L[i])
            i += 1

    def test_min(self):
        self.assertEqual(self.bst.min(), min(self.L))

    def test_max(self):
        self.assertEqual(self.bst.max(), max(self.L))

    def test_delete_min(self):
        self.bst.delete_min()
        self.assertEqual(self.bst.min(), min(self.L[1:]))

    def test_delete_max(self):
        self.bst.delete_max()
        self.assertEqual(self.bst.max(), max(self.L[:-1]))

    def test_range(self):
        R = [6, 7, 10, 13]
        i = 0
        for x in self.bst.range_keys(5, 13):
            self.assertEqual(x, R[i])
            i += 1


class HugeBSTMethods(unittest.TestCase):
    def setUp(self):
        random.seed(0)

        self.L = random.sample(range(10 ** 6), 10 ** 4)
        self.S = sorted(self.L)
        self.bst = BST()
        for x in self.L:
            self.bst.put(x, x)

    def test_put_and_get(self):
        st = self.bst
        for x in st.keys():
            self.assertEqual(st.get(x), x)
        for x in st.keys():
            st.put(x, st.get(x) - 1)
        for x in st.keys():
            self.assertEqual(st.get(x), x - 1)

    def test_keys(self):
        i = 0
        for x in self.bst.keys():
            self.assertEqual(x, self.S[i])
            i += 1

    def test_min(self):
        self.assertEqual(self.bst.min(), min(self.L))

    def test_max(self):
        self.assertEqual(self.bst.max(), max(self.L))

    def test_delete_min(self):
        self.bst.delete_min()
        self.assertEqual(self.bst.min(), min(self.S[1:]))

    def test_delete_max(self):
        self.bst.delete_max()
        self.assertEqual(self.bst.max(), max(self.S[:-1]))

    def test_min_priority_queue(self):
        i = 0
        while not self.bst.is_empty():
            self.assertEqual(self.S[i], self.bst.min())
            self.bst.delete_min()
            i += 1

    def test_max_priority_queue(self):
        i = len(self.S) - 1
        while not self.bst.is_empty():
            self.assertEqual(self.S[i], self.bst.max())
            self.bst.delete_max()
            i -= 1

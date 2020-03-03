import unittest

from itu.algs4.fundamentals.binary_search import index_of


class TestBinarySearchMethods(unittest.TestCase):
    def setUp(self):
        self.a = [0,1,2,3,4,5,6,7,8,9]
        self.b = [0,0,1,1,2,2,3,3,4,4]
        self.c = [1]
        self.d = []

    def test_index_of(self):
        self.assertEqual(index_of(self.a, 4), 4)
        self.assertEqual(index_of(self.a, 10), -1)
        self.assertEqual(index_of(self.a, -1), -1)
        self.assertEqual(index_of(self.b, 0), 0 or 1)
        self.assertEqual(index_of(self.b, 20), -1)
        self.assertEqual(index_of(self.c, 1), 0)
        self.assertEqual(index_of(self.c, 0), -1)
        self.assertEqual(index_of(self.d, 0), -1)
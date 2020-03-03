import unittest

from itu.algs4.fundamentals.bag import Bag

class TestBagMethods(unittest.TestCase):
    def setUp(self):
        self.bag = Bag()

    def test_add(self):
        self.bag.add(-1)
        self.bag.add(2147483648)
        self.bag.add(0)
        self.assertEqual(self.bag.size(), 3)

    def test_is_empty(self):
        self.assertTrue(self.bag.is_empty())
        self.bag.add(1)
        self.assertFalse(self.bag.is_empty())

    def test_size_and_len(self):
        for i in range(100):
            self.assertEqual(self.bag.size(), i)
            self.assertEqual(len(self.bag), i) # Currently just calls size()
            self.bag.add(i)

    def test_iter(self):
        for i in range(10):
            self.bag.add(i)
        l = []
        for i in iter(self.bag):
            l.append(i)
        for i in range(10):
            self.assertIn(i,l)
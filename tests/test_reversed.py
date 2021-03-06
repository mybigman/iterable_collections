import unittest

from iterable_collections import collect


class TestReversed(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10))).reversed()
        self.assertEqual(c.list(), list(reversed(list(list(range(10))))))

    def test_set(self):
        c = collect(set(range(10))).reversed()
        self.assertEqual(c.list(), list(reversed(list(set(range(10))))))

    def test_tuple(self):
        c = collect(tuple(range(10))).reversed()
        self.assertEqual(c.list(), list(reversed(list(tuple(range(10))))))

    def test_iterator(self):
        c = collect(iter(range(10))).reversed()
        self.assertEqual(c.list(), list(reversed(list(iter(range(10))))))

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).reversed()
        self.assertEqual(c.list(), list(reversed(list({'a': 1, 'b': 2}))))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items()).reversed()
        self.assertEqual(c.list(), list(reversed(list({'a': 1, 'b': 2}.items()))))

    def test_enumerate(self):
        c = collect(list(range(10))).enumerate().reversed()
        self.assertEqual(c.list(), list(reversed(list(enumerate(range(10))))))

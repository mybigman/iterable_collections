import unittest

from iterable_collections import collect


class TestEnumerate(unittest.TestCase):

    def test_list(self):
        c = collect(list(range(10))).enumerate()

        self.assertEqual(c.list(), list(enumerate(range(10))))

    def test_set(self):
        c = collect(set(range(10))).enumerate()
        self.assertEqual(c.list(), list(enumerate(range(10))))

    def test_tuple(self):
        c = collect(tuple(range(10))).enumerate()
        self.assertEqual(c.list(), list(enumerate(range(10))))

    def test_iterator(self):
        c = collect(iter(range(10))).enumerate()
        self.assertEqual(c.list(), list(enumerate(range(10))))

    def test_dict(self):
        c = collect({'a': 1, 'b': 2}).enumerate()
        self.assertEqual(c.list(), list(enumerate({'a': 1, 'b': 2})))

    def test_dict_items(self):
        c = collect({'a': 1, 'b': 2}.items()).enumerate()
        self.assertEqual(c.list(), list(enumerate({'a': 1, 'b': 2}.items())))


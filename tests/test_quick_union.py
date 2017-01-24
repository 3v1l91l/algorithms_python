from unittest import TestCase

from algorithms.union_find import (
    quick_union,
)

class TestQuickUnion(TestCase):
    def test_finds_connected(self):
        qf = quick_union.QuickUnion(4)

        qf.union(0,1)
        qf.union(2,3)

        self.assertEqual(True, qf.connected(0,1))
        self.assertEqual(True, qf.connected(2,3))
        self.assertEqual(False, qf.connected(0,2))

    def test_finds_connection_in_groups(self):
        qf = quick_union.QuickUnion(5)

        qf.union(0,1)
        qf.union(2,3)
        qf.union(1,2)
        qf.union(0,4)

        self.assertEqual(True, qf.connected(0,2))
        self.assertEqual(True, qf.connected(1,4))

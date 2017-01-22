from unittest import TestCase

from algorithms.sort import (
     selection,
)

class TestSelectionSort(TestCase):
    def test_list_with_unique_items(self):
        self.sortList = list(range(9, -1, -1))

        sortedList = selection.sort(self.sortList)
        self.assertEqual(sortedList, list(range(0, 10)))

    def test_list_with_not_unique_items(self):
        self.sortList = [5,2,1,4,3,2,5];

        sortedList = selection.sort(self.sortList)
        self.assertEqual(sortedList, [1,2,2,3,4,5,5])


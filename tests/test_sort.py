from unittest import TestCase

from algorithms.sort import (
     selection,
)

class TestSelectionSort(TestCase):
    def test_list_with_unique_items(self):
        self.sortList = list(range(9, -1, -1))

        sortedList = selection.sort(self.sortList)
        self.assertIs(sortedList, list(range(0, 10)))

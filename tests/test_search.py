from unittest import TestCase

from algorithms.search import (
     binary,
)

class TestBinarySearch(TestCase):
    def test_range_with_no_search_item(self):
        self.searchList = range(0,10)

        foundIndex = binary.search(self.searchList, -1)
        self.assertIs(foundIndex, False)

    def test_range_with_search_items(self):
        self.searchList = range(0,10)

        foundIndex = binary.search(self.searchList, 0)
        self.assertIs(foundIndex, 0)

        foundIndex = binary.search(self.searchList, 5)
        self.assertIs(foundIndex, 5)

        foundIndex = binary.search(self.searchList, 9)
        self.assertIs(foundIndex, 9)
import unittest

from BinarySearch.q035_search_insert_position import Solution


class TestSearchInsertPosition(unittest.TestCase):
    """Test q035_search_insert_position.py"""

    def test_search_insert_position(self):
        s = Solution()

        self.assertEqual(2, s.searchInsert([1, 3, 5, 6], 5))
        self.assertEqual(1, s.searchInsert([1, 3, 5, 6], 2))
        self.assertEqual(4, s.searchInsert([1, 3, 5, 6], 7))
        self.assertEqual(0, s.searchInsert([1, 3, 5, 6], 0))


if __name__ == '__main__':
    unittest.main()

import unittest

from BinarySearch.q081_search_in_rotated_sorted_array_ii import Solution


class TestSearchInRotatedSortedArrayIi(unittest.TestCase):
    """Test q081_search_in_rotated_sorted_array_ii.py"""

    def test_search_in_rotated_sorted_array_ii(self):
        s = Solution()

        self.assertEqual(True, s.search([2, 5, 6, 0, 0, 1, 2], 0))
        self.assertEqual(False, s.search([2, 5, 6, 0, 0, 1, 2], 3))
        self.assertEqual(True, s.search([1, 1, 3, 1], 3))
        self.assertEqual(True, s.search([1, 3, 1, 1, 1], 3))


if __name__ == '__main__':
    unittest.main()

import unittest

from BinarySearch.q033_search_in_rotated_sorted_array import Solution


class TestSearchInRotatedSortedArray(unittest.TestCase):
    """Test q033_search_in_rotated_sorted_array.py"""

    def test_search_in_rotated_sorted_array(self):
        s = Solution()

        self.assertEqual(4, s.search([4, 5, 6, 7, 0, 1, 2], 0))
        self.assertEqual(5, s.search([4, 5, 6, 7, 0, 1, 2], 1))
        self.assertEqual(3, s.search([4, 5, 6, 7, 0, 1, 2], 7))
        self.assertEqual(0, s.search([4, 5, 6, 7, 0, 1, 2], 4))
        self.assertEqual(1, s.search([4, 5, 6, 7, 0, 1, 2], 5))
        self.assertEqual(0, s.search([0, 1, 2, 4, 5, 6, 7], 0))
        self.assertEqual(6, s.search([0, 1, 2, 4, 5, 6, 7], 7))
        self.assertEqual(3, s.search([0, 1, 2, 4, 5, 6, 7], 4))
        self.assertEqual(-1, s.search([4, 5, 6, 7, 0, 1, 2], 3))


if __name__ == '__main__':
    unittest.main()

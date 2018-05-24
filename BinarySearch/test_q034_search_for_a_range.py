import unittest

from BinarySearch.q034_search_for_a_range import Solution


class TestSearchForARange(unittest.TestCase):
    """Test q034_search_for_a_range.py"""

    def test_search_for_a_range(self):
        s = Solution()

        self.assertEqual([3, 4], s.searchRange([5, 7, 7, 8, 8, 10], 8))
        self.assertEqual([-1, -1], s.searchRange([5, 7, 7, 8, 8, 10], 6))
        self.assertEqual([0, 4], s.searchRange([8, 8, 8, 8, 8], 8))
        self.assertEqual([-1, -1], s.searchRange([], 8))
        self.assertEqual([0, 0], s.searchRange([8], 8))
        self.assertEqual([-1, -1], s.searchRange([7], 8))
        self.assertEqual([-1, -1], s.searchRange([6, 7], 8))


if __name__ == '__main__':
    unittest.main()

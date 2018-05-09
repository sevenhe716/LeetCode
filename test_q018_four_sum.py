import unittest

from q018_four_sum import Solution


class TestFourSumClosest(unittest.TestCase):
    """Test q018_four_sum.py"""

    def test_four_sum_closest(self):
        s = Solution()

        self.assertEqual(sorted([[-2, -2, 2, 2], [-1, -1, 0, 2], [-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]), sorted(s.fourSum([1, -1, -2, 2, 0, -1, 0, -2, 2], 0)))
        self.assertEqual([], sorted(s.fourSum([1, 0, -1, 0, -2, 2], 10)))
        self.assertEqual([[0, 0, 0, 0]], sorted(s.fourSum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)))
        self.assertEqual(sorted([[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, -1, 0, 2]]), sorted(s.fourSum([1, 0, -1, -1, 0, -1, 0, -2, 2], 0)))


if __name__ == '__main__':
    unittest.main()

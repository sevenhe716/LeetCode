import unittest

from BackTracking.q040_combination_sum_ii import Solution


class TestCombinationSumIi(unittest.TestCase):
    """Test q040_combination_sum_ii.py"""

    def test_combination_sum_ii(self):
        s = Solution()

        self.assertEqual(sorted([
            [1, 7],
            [1, 2, 5],
            [2, 6],
            [1, 1, 6]
        ]), sorted(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)))

        self.assertEqual(sorted([
            [1, 2, 2],
            [5]
        ]), sorted(s.combinationSum2([2, 5, 2, 1, 2], 5)))


if __name__ == '__main__':
    unittest.main()

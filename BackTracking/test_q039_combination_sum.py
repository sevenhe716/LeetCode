import unittest

from BackTracking.q039_combination_sum import Solution


class TestCombinationSum(unittest.TestCase):
    """Test q039_combination_sum.py"""

    def test_combination_sum(self):
        s = Solution()

        self.assertSequenceEqual(sorted([
            [7],
            [2, 2, 3]
        ]), sorted(s.combinationSum([2, 3, 6, 7], 7)))

        self.assertSequenceEqual(sorted([
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5]
        ]), sorted(s.combinationSum([2, 3, 5], 8)))

        self.assertSequenceEqual(sorted([
        ]), sorted(s.combinationSum([], 1)))

        self.assertSequenceEqual(sorted([
            [1],
        ]), sorted(s.combinationSum([1], 1)))


if __name__ == '__main__':
    unittest.main()

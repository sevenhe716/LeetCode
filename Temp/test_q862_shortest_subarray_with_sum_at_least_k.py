import unittest

from q862_shortest_subarray_with_sum_at_least_k import Solution


class TestShortestSubarrayWithSumAtLeastK(unittest.TestCase):
    """Test q862_shortest_subarray_with_sum_at_least_k.py"""

    def test_shortest_subarray_with_sum_at_least_k(self):
        s = Solution()

        self.assertEqual(1, s.shortestSubarray([1], 1))
        self.assertEqual(-1, s.shortestSubarray([1, 2], 4))
        self.assertEqual(3, s.shortestSubarray([2, -1, 2], 3))
        self.assertEqual(1, s.shortestSubarray([77, 19, 35, 10, -14], 19))
        self.assertEqual(2, s.shortestSubarray([48, 99, 37, 4, -31], 140))
        self.assertEqual(2, s.shortestSubarray([17, 85, 93, -45, -21], 150))
        self.assertEqual(2, s.shortestSubarray([56, -21, 56, 35, -9], 61))


if __name__ == '__main__':
    unittest.main()

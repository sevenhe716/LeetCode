import unittest

from DivideAndConquer.q053_maximum_subarray import Solution


class TestMaximumSubarray(unittest.TestCase):
    """Test q053_maximum_subarray.py"""

    def test_maximum_subarray(self):
        s = Solution()

        self.assertEqual(6, s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(-1, s.maxSubArray([-2, -3, -1, -5]))
        self.assertEqual(-2, s.maxSubArray([-2]))


if __name__ == '__main__':
    unittest.main()

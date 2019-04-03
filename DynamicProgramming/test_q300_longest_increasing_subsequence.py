import unittest

from DynamicProgramming.q300_longest_increasing_subsequence import Solution


class TestLongestIncreasingSubsequence(unittest.TestCase):
    """Test q300_longest_increasing_subsequence.py"""

    def test_longest_increasing_subsequence(self):
        s = Solution()

        self.assertEqual(4, s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))


if __name__ == '__main__':
    unittest.main()

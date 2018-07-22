import unittest

from DynamicProgramming.q873_length_of_longest_fibonacci_subsequence import Solution


class TestLengthOfLongestFibonacciSubsequence(unittest.TestCase):
    """Test q873_length_of_longest_fibonacci_subsequence.py"""

    def test_length_of_longest_fibonacci_subsequence(self):
        s = Solution()

        self.assertEqual(5, s.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertEqual(3, s.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))


if __name__ == '__main__':
    unittest.main()

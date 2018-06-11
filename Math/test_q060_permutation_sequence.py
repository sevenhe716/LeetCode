import unittest

from Math.q060_permutation_sequence import Solution


class TestPermutationSequence(unittest.TestCase):
    """Test q060_permutation_sequence.py"""

    def test_permutation_sequence(self):
        s = Solution()

        self.assertEqual('123', s.getPermutation(3, 1))
        self.assertEqual('321', s.getPermutation(3, 6))
        self.assertEqual('213', s.getPermutation(3, 3))
        self.assertEqual('2314', s.getPermutation(4, 9))


if __name__ == '__main__':
    unittest.main()

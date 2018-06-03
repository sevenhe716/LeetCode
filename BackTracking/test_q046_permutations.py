import unittest

from BackTracking.q046_permutations import Solution2


class TestPermutations(unittest.TestCase):
    """Test q046_permutations.py"""

    def test_permutations(self):
        s = Solution2()

        self.assertSequenceEqual(sorted([[1, 2, 3],
                                         [1, 3, 2],
                                         [2, 1, 3],
                                         [2, 3, 1],
                                         [3, 1, 2],
                                         [3, 2, 1]]), s.permute([1, 2, 3]))

        self.assertSequenceEqual([[1]], s.permute([1]))

        self.assertSequenceEqual([], s.permute([]))


if __name__ == '__main__':
    unittest.main()

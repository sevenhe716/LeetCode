import unittest

from DFS.q047_permutations_ii import Solution


class TestPermutationsIi(unittest.TestCase):
    """Test q047_permutations_ii.py"""

    def test_permutations_ii(self):
        s = Solution()

        self.assertSequenceEqual(sorted(
            [[0, 0, 0, 1, 9], [0, 0, 0, 9, 1], [0, 0, 1, 0, 9], [0, 0, 1, 9, 0], [0, 0, 9, 0, 1], [0, 0, 9, 1, 0],
             [0, 1, 0, 0, 9], [0, 1, 0, 9, 0], [0, 1, 9, 0, 0], [0, 9, 0, 0, 1], [0, 9, 0, 1, 0], [0, 9, 1, 0, 0],
             [1, 0, 0, 0, 9], [1, 0, 0, 9, 0], [1, 0, 9, 0, 0], [1, 9, 0, 0, 0], [9, 0, 0, 0, 1], [9, 0, 0, 1, 0],
             [9, 0, 1, 0, 0], [9, 1, 0, 0, 0]]), sorted(s.permuteUnique([0, 1, 0, 0, 9])))

        self.assertSequenceEqual(sorted([
            [1, 1, 2],
            [1, 2, 1],
            [2, 1, 1]
        ]), sorted(s.permuteUnique([1, 1, 2])))

        self.assertSequenceEqual(sorted([
            [1, 1]
        ]), sorted(s.permuteUnique([1, 1])))

        self.assertSequenceEqual(sorted([
            [1]
        ]), sorted(s.permuteUnique([1])))

        self.assertSequenceEqual(sorted([]), sorted(s.permuteUnique([])))


if __name__ == '__main__':
    unittest.main()

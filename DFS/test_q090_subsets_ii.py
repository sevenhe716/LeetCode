import unittest

from DFS.q090_subsets_ii import Solution


class TestSubsetsIi(unittest.TestCase):
    """Test q090_subsets_ii.py"""

    def test_subsets_ii(self):
        s = Solution()

        self.assertEqual(sorted([
            [2],
            [1],
            [1, 2, 2],
            [2, 2],
            [1, 2],
            []
        ]), sorted(s.subsetsWithDup([1, 2, 2])))


if __name__ == '__main__':
    unittest.main()

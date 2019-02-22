import unittest

from DFS.q078_subsets import Solution


class TestSubsets(unittest.TestCase):
    """Test q078_subsets.py"""

    def test_subsets(self):
        s = Solution()

        self.assertEqual(sorted([
            [3],
            [1],
            [2],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            []
        ]), sorted(s.subsets([1, 2, 3])))


if __name__ == '__main__':
    unittest.main()

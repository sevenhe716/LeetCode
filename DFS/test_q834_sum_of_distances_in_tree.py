import unittest

from DFS.q834_sum_of_distances_in_tree import Solution


class TestSumOfDistancesInTree(unittest.TestCase):
    """Test q834_sum_of_distances_in_tree.py"""

    def test_sum_of_distances_in_tree(self):
        s = Solution()
        self.assertEqual([0], s.sumOfDistancesInTree(1, []))
        self.assertEqual([1, 1], s.sumOfDistancesInTree(2, [[0, 1]]))
        self.assertEqual([8, 12, 6, 10, 10, 10], s.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
        self.assertEqual([18, 25, 13, 14, 20, 20, 21, 19, 26],
                         s.sumOfDistancesInTree(9, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5], [3, 6], [3, 7], [7, 8]]))


if __name__ == '__main__':
    unittest.main()

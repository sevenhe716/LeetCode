import unittest

from q863_all_nodes_distance_k_in_binary_tree import Solution


class TestAllNodesDistanceKInBinaryTree(unittest.TestCase):
    """Test q863_all_nodes_distance_k_in_binary_tree.py"""

    def test_all_nodes_distance_k_in_binary_tree(self):
        s = Solution()

        self.assertEqual([7, 4, 1], s.distanceK([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 2))


if __name__ == '__main__':
    unittest.main()

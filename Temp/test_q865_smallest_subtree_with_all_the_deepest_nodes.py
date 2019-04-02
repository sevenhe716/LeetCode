import unittest

from Temp.q865_smallest_subtree_with_all_the_deepest_nodes import Solution


class TestSmallestSubtreeWithAllTheDeepestNodes(unittest.TestCase):
    """Test q865_smallest_subtree_with_all_the_deepest_nodes.py"""

    def test_smallest_subtree_with_all_the_deepest_nodes(self):
        s = Solution()

        self.assertEqual([2, 7, 4], s.subtreeWithAllDeepest([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]))


if __name__ == '__main__':
    unittest.main()

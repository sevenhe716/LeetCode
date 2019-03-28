import unittest

from BST.q270_closest_binary_search_tree_value import Solution
from common import TreeNode


class TestClosestBinarySearchTreeValue(unittest.TestCase):
    """Test q270_closest_binary_search_tree_value.py"""

    def test_closest_binary_search_tree_value(self):
        s = Solution()

        self.assertEqual(4, s.closestValue(TreeNode.generate([4, 2, 5, 1, 3]), 3.714286))


if __name__ == '__main__':
    unittest.main()

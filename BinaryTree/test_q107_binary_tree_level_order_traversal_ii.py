import unittest

from BinaryTree.q107_binary_tree_level_order_traversal_ii import Solution1
from common import TreeNode


class TestBinaryTreeLevelOrderTraversalIi(unittest.TestCase):
    """Test q107_binary_tree_level_order_traversal_ii.py"""

    def test_binary_tree_level_order_traversal_ii(self):
        s = Solution1()

        self.assertEqual([[15, 7], [9, 20], [3]], s.levelOrderBottom(TreeNode.generate([3, 9, 20, None, None, 15, 7])))
        self.assertEqual([], s.levelOrderBottom(TreeNode.generate([])))
        self.assertEqual([[4, 5], [2, 3], [1]], s.levelOrderBottom(TreeNode.generate([1, 2, 3, 4, 5])))


if __name__ == '__main__':
    unittest.main()

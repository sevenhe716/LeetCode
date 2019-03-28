import unittest

from BinaryTree.q314_binary_tree_vertical_order_traversal import Solution
from common import TreeNode


class TestBinaryTreeVerticalOrderTraversal(unittest.TestCase):
    """Test q314_binary_tree_vertical_order_traversal.py"""

    def test_binary_tree_vertical_order_traversal(self):
        s = Solution()

        self.assertEqual([
            [9],
            [3, 15],
            [20],
            [7]
        ], s.verticalOrder(TreeNode.generate([3, 9, 20, None, None, 15, 7])))

        self.assertEqual([
            [4],
            [9],
            [3, 0, 1],
            [8],
            [7]
        ], s.verticalOrder(TreeNode.generate([3, 9, 8, 4, 0, 1, 7])))

        self.assertEqual([
            [4],
            [9, 5],
            [3, 0, 1],
            [8, 2],
            [7]
        ], s.verticalOrder(TreeNode.generate([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5])))


if __name__ == '__main__':
    unittest.main()

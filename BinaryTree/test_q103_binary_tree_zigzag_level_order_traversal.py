import unittest

from BinaryTree.q103_binary_tree_zigzag_level_order_traversal import Solution
from common import TreeNode


class TestBinaryTreeZigzagLevelOrderTraversal(unittest.TestCase):
    """Test q103_binary_tree_zigzag_level_order_traversal.py"""

    def test_binary_tree_zigzag_level_order_traversal(self):
        s = Solution()

        self.assertEqual([
            [3],
            [20, 9],
            [15, 7]
        ], s.zigzagLevelOrder(TreeNode.generate([3, 9, 20, None, None, 15, 7])))


if __name__ == '__main__':
    unittest.main()

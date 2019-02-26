import unittest

from Tree.q102_binary_tree_level_order_traversal import Solution
from common import TreeNode


class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    """Test q102_binary_tree_level_order_traversal.py"""

    def test_binary_tree_level_order_traversal(self):
        s = Solution()

        self.assertEqual([
            [3],
            [9, 20],
            [15, 7]
        ], s.levelOrder(TreeNode.generate([3, 9, 20, None, None, 15, 7])))


if __name__ == '__main__':
    unittest.main()

import unittest

from Tree.q105_construct_binary_tree_from_preorder_and_inorder_traversal import Solution
from common import TreeNode


class TestConstructBinaryTreeFromPreorderAndInorderTraversal(unittest.TestCase):
    """Test q105_construct_binary_tree_from_preorder_and_inorder_traversal.py"""

    def test_construct_binary_tree_from_preorder_and_inorder_traversal(self):
        s = Solution()

        self.assertEqual(TreeNode.generate([3, 9, 20, None, None, 15, 7]),
                         s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))


if __name__ == '__main__':
    unittest.main()

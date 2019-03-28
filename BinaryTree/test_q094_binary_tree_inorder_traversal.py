import unittest

from BinaryTree.q094_binary_tree_inorder_traversal import Solution
from common import TreeNode


class TestBinaryTreeInorderTraversal(unittest.TestCase):
    """Test q094_binary_tree_inorder_traversal.py"""

    def test_binary_tree_inorder_traversal(self):
        s = Solution()

        self.assertEqual([1, 3, 2], s.inorderTraversal(TreeNode.generate([1, None, 2, None, None, 3])))
        self.assertEqual([4, 2, 5, 1, 6, 3, 7], s.inorderTraversal(TreeNode.generate([1, 2, 3, 4, 5, 6, 7])))
        self.assertEqual([4, 2, 8, 5, 9, 1, 6, 3, 7], s.inorderTraversal(TreeNode.generate([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9])))

        self.assertEqual([1, 2, 3], s.preorderTraversal(TreeNode.generate([1, None, 2, None, None, 3])))
        self.assertEqual([1, 2, 4, 5, 3, 6, 7], s.preorderTraversal(TreeNode.generate([1, 2, 3, 4, 5, 6, 7])))
        self.assertEqual([1, 2, 4, 5, 8, 9, 3, 6, 7], s.preorderTraversal(TreeNode.generate([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9])))

        self.assertEqual([3, 2, 1], s.postorderTraversal(TreeNode.generate([1, None, 2, None, None, 3])))
        self.assertEqual([4, 5, 2, 6, 7, 3, 1], s.postorderTraversal(TreeNode.generate([1, 2, 3, 4, 5, 6, 7])))
        self.assertEqual([4, 8, 9, 5, 2, 6, 7, 3, 1], s.postorderTraversal(TreeNode.generate([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9])))

    if __name__ == '__main__':
        unittest.main()

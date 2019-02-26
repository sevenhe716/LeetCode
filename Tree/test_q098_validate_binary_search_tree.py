import unittest

from Tree.q098_validate_binary_search_tree import Solution
from common import TreeNode


class TestValidateBinarySearchTree(unittest.TestCase):
    """Test q098_validate_binary_search_tree.py"""

    def test_validate_binary_search_tree(self):
        s = Solution()

        self.assertEqual(True, s.isValidBST(TreeNode.generate([])))
        self.assertEqual(True, s.isValidBST(TreeNode.generate([2, 1, 3])))
        self.assertEqual(False, s.isValidBST(TreeNode.generate([5, 1, 4, None, None, 3, 6])))
        self.assertEqual(False, s.isValidBST(TreeNode.generate([10, 5, 15, None, None, 6, 20])))
        self.assertEqual(True, s.isValidBST(TreeNode.generate([0, -1])))


if __name__ == '__main__':
    unittest.main()

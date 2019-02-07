import unittest

from Tree.q110_balanced_binary_tree import Solution
from common import TreeNode


class TestBalancedBinaryTree(unittest.TestCase):
    """Test q110_balanced_binary_tree.py"""

    def test_balanced_binary_tree(self):
        s = Solution()

        self.assertEqual(True, s.isBalanced(TreeNode.generate([3, 9, 20, None, None, 15, 7])))
        self.assertEqual(False, s.isBalanced(TreeNode.generate([1, 2, 2, 3, 3, None, None, 4, 4])))


if __name__ == '__main__':
    unittest.main()

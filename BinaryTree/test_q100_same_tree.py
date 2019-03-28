import unittest

from BinaryTree.q100_same_tree import Solution
from common import TreeNode

class TestSameTree(unittest.TestCase):
    """Test q100_same_tree.py"""

    def test_same_tree(self):
        s = Solution()

        self.assertEqual(True, s.isSameTree(TreeNode.generate([1, 2, 3]), TreeNode.generate([1, 2, 3])))
        self.assertEqual(False, s.isSameTree(TreeNode.generate([1, 2]), TreeNode.generate([1, None, 2])))
        self.assertEqual(False, s.isSameTree(TreeNode.generate([1, 2, 1]), TreeNode.generate([1, 1, 2])))

if __name__ == '__main__':
    unittest.main()

import unittest

from BinaryTree.q112_path_sum import Solution
from common import TreeNode


class TestPathSum(unittest.TestCase):
    """Test q112_path_sum.py"""

    def test_path_sum(self):
        s = Solution()

        self.assertEqual(True, s.hasPathSum(
            TreeNode.generate([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]), 22))
        self.assertEqual(True, s.hasPathSum(TreeNode.generate([]), 0))
        self.assertEqual(False, s.hasPathSum(TreeNode.generate([]), 1))

if __name__ == '__main__':
    unittest.main()

import unittest

from Mock.m4131_microsoft import Solution
from common import TreeNode


class TestMicrosoft(unittest.TestCase):
    """Test m4131_microsoft.py"""

    def test_microsoft(self):
        s = Solution()
        self.assertEqual(TreeNode.generate(
            [36, 34, 42, 33, 35, 41, 43, 32, None, None, None, 37, None, None, 44, None, None, None, 38, None, None,
             None, 39, None, 40]), s.trimBST(TreeNode.generate(
            [45, 30, 46, 10, 36, None, 49, 8, 24, 34, 42, 48, None, 4, 9, 14, 25, 31, 35, 41, 43, 47, None, 0, 6, None,
             None, 11, 20, None, 28, None, 33, None, None, 37, None, None, 44, None, None, None, 1, 5, 7, None, 12, 19,
             21,
             26, 29, 32, None, None, 38, None, None, None, 3, None, None, None, None, None, 13, 18, None, None, 22,
             None,
             27, None, None, None, None, None, 39, 2, None, None, None, 15, None, None, 23, None, None, None, 40, None,
             None, None, 16, None, None, None, None, None, 17]), 32, 44))

        self.assertEqual(TreeNode.generate([1, None, 2]), s.trimBST(TreeNode.generate([3, 1, 4, None, 2]), 1, 2))
        self.assertEqual(TreeNode.generate([1, None, 2]), s.trimBST(TreeNode.generate([1, 0, 2]), 1, 2))
        self.assertEqual(TreeNode.generate([3, 2, None, 1]),
                         s.trimBST(TreeNode.generate([3, 0, 4, None, 2, None, None, None, None, 1]), 1, 3))

        if __name__ == '__main__':
            unittest.main()

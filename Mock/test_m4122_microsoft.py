import unittest

from Mock.m4122_microsoft import Solution
from common import TreeNode


class TestMicrosoft(unittest.TestCase):
    """Test m4122_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(2, s.inorderSuccessor(TreeNode.generate([2, 1, 3]), 1))
        self.assertEqual(None, s.inorderSuccessor(TreeNode.generate([[5, 3, 6, 2, 4, None, None, 1]]), 6))


if __name__ == '__main__':
    unittest.main()

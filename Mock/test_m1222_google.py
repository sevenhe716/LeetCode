import unittest

from Mock.m1222_google import Solution
from common import TreeNode


class TestGoogle(unittest.TestCase):
    """Test m1222_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual(0, s.countNodes(TreeNode.generate([])))
        self.assertEqual(6, s.countNodes(TreeNode.generate([1, 2, 3, 4, 5, 6])))


if __name__ == '__main__':
    unittest.main()

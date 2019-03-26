import unittest

from Mock.m2223_facebook import Solution
from common import TreeNode


class TestFacebook(unittest.TestCase):
    """Test m2223_facebook.py"""

    def test_facebook(self):
        s = Solution()

        self.assertEqual([
            [9],
            [3, 15],
            [20],
            [7]
        ], s.verticalOrder(TreeNode.generate([3, 9, 20, None, None, 15, 7])))
        self.assertEqual([
            [4],
            [9],
            [3, 0, 1],
            [8],
            [7]
        ], s.verticalOrder(TreeNode.generate([3, 9, 8, 4, 0, 1, 7])))
        self.assertEqual([
            [4],
            [9, 5],
            [3, 0, 1],
            [8, 2],
            [7]
        ], s.verticalOrder(TreeNode.generate([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5])))

    if __name__ == '__main__':
        unittest.main()

import unittest

from Mock.m3231_amazon import Solution
from common import TreeNode


class TestAmazon(unittest.TestCase):
    """Test m3231_amazon.py"""

    def test_amazon(self):
        s = Solution()

        self.assertEqual(True, s.isValidBST(TreeNode.generate([2, 1, 3])))
        self.assertEqual(False, s.isValidBST(TreeNode.generate([5, 1, 4, None, None, 3, 6])))


if __name__ == '__main__':
    unittest.main()

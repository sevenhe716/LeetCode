import unittest

from BinaryTree.q437_path_sum_iii import Solution
from common import TreeNode


class TestPathSumIii(unittest.TestCase):
    """Test q437_path_sum_iii.py"""

    def test_path_sum_iii(self):
        s = Solution()

        self.assertEqual(3, s.pathSum(TreeNode.generate([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8))


if __name__ == '__main__':
    unittest.main()

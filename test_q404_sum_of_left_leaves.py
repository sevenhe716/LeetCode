import unittest

from q404_sum_of_left_leaves import Solution
from common import TreeNode


class TestSumOfLeftLeaves(unittest.TestCase):
    """Test q404_sum_of_left_leaves.py"""

    def test_sum_of_left_leaves(self):
        s = Solution()

        self.assertEqual(0, s.sumOfLeftLeaves(TreeNode.generate([1])))
        self.assertEqual(24, s.sumOfLeftLeaves(TreeNode.generate([3, 9, 20, None, None, 15, 7])))


if __name__ == '__main__':
    unittest.main()

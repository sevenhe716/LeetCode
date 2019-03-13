import unittest

from Tree.q617_merge_two_binary_trees import Solution
from common import TreeNode


class TestMergeTwoBinaryTrees(unittest.TestCase):
    """Test q617_merge_two_binary_trees.py"""

    def test_merge_two_binary_trees(self):
        s = Solution()
        self.assertEqual(TreeNode.generate([3, 4, 5, 5, 4, None, 7]),
                         s.mergeTrees(TreeNode.generate([1, 3, 2, 5]), TreeNode.generate([2, 1, 3, None, 4, None, 7])))


if __name__ == '__main__':
    unittest.main()

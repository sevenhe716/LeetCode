import unittest

from BFS.q111_minimum_depth_of_binary_tree import Solution
from common import TreeNode


class TestMinimumDepthOfBinaryTree(unittest.TestCase):
    """Test q111_minimum_depth_of_binary_tree.py"""

    def test_minimum_depth_of_binary_tree(self):
        s = Solution()

        self.assertEqual(2, s.minDepth(TreeNode.generate([3, 9, 20, None, None, 15, 7])))
        self.assertEqual(2, s.minDepth(TreeNode.generate([1, 2])))


if __name__ == '__main__':
    unittest.main()

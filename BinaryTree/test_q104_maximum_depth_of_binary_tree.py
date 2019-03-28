import unittest

from BinaryTree.q104_maximum_depth_of_binary_tree import Solution
from common import TreeNode

class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    """Test q104_maximum_depth_of_binary_tree.py"""

    def test_maximum_depth_of_binary_tree(self):
        s = Solution()

        self.assertEqual(0, s.maxDepth(TreeNode.generate([])))
        self.assertEqual(3, s.maxDepth(TreeNode.generate([3, 9, 20, None, None, 15, 7])))


if __name__ == '__main__':
    unittest.main()

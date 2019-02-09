import unittest

from Tree.q257_binary_tree_paths import Solution
from common import TreeNode


class TestBinaryTreePaths(unittest.TestCase):
    """Test q257_binary_tree_paths.py"""

    def test_binary_tree_paths(self):
        s = Solution()

        self.assertEqual([], s.binaryTreePaths([]))
        self.assertEqual(["1->2->5", "1->3"], s.binaryTreePaths(TreeNode.generate([1, 2, 3, None, 5])))


if __name__ == '__main__':
    unittest.main()

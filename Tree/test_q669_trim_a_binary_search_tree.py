import unittest

from Tree.q669_trim_a_binary_search_tree import Solution
from common import TreeNode


class TestTrimABinarySearchTree(unittest.TestCase):
    """Test q669_trim_a_binary_search_tree.py"""

    def test_trim_a_binary_search_tree(self):
        s = Solution()

        self.assertEqual(TreeNode.generate([1, None, 2]), s.trimBST(TreeNode.generate([3, 1, 4, None, 2]), 1, 2))
        self.assertEqual(TreeNode.generate([1, None, 2]), s.trimBST(TreeNode.generate([1, 0, 2]), 1, 2))
        self.assertEqual(TreeNode.generate([3, 2, None, 1]),
                         s.trimBST(TreeNode.generate([3, 0, 4, None, 2, None, None, None, None, 1]), 1, 3))


if __name__ == '__main__':
    unittest.main()

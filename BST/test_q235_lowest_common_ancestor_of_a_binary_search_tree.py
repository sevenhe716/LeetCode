import unittest

from BST.q235_lowest_common_ancestor_of_a_binary_search_tree import Solution
from common import TreeNode


class TestLowestCommonAncestorOfABinarySearchTree(unittest.TestCase):
    """Test q235_lowest_common_ancestor_of_a_binary_search_tree.py"""

    def test_lowest_common_ancestor_of_a_binary_search_tree(self):
        s = Solution()

        self.assertEqual(6,
                         s.lowestCommonAncestor(TreeNode.generate([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), 2, 8).val)
        self.assertEqual(2,
                         s.lowestCommonAncestor(TreeNode.generate([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), 2, 4).val)


if __name__ == '__main__':
    unittest.main()

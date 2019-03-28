import unittest

from BST.q108_convert_sorted_array_to_binary_search_tree import Solution
from common import TreeNode


class TestConvertSortedArrayToBinarySearchTree(unittest.TestCase):
    """Test q108_convert_sorted_array_to_binary_search_tree.py"""

    def test_convert_sorted_array_to_binary_search_tree(self):
        s = Solution()

        self.assertEqual(TreeNode.generate([0, -3, 9, -10, None, 5]), s.sortedArrayToBST([-10, -3, 0, 5, 9]))

if __name__ == '__main__':
    unittest.main()

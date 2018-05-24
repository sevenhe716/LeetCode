import unittest

from Tree.q515_find_largest_value_in_each_tree_row import Solution
from common import TreeNode


class TestFindLargestValueInEachTreeRow(unittest.TestCase):
    """Test q515_find_largest_value_in_each_tree_row.py"""

    def test_find_largest_value_in_each_tree_row(self):
        s = Solution()

        root = TreeNode(1)
        root.left = TreeNode(3)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(3)
        root.right = TreeNode(2)
        root.right.right = TreeNode(9)
        self.assertEqual([1, 3, 9], s.largestValues(root))


if __name__ == '__main__':
    unittest.main()

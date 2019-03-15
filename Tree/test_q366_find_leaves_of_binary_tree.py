import unittest

from Tree.q366_find_leaves_of_binary_tree import Solution1
from common import TreeNode


class TestFindLeavesOfBinaryTree(unittest.TestCase):
    """Test q366_find_leaves_of_binary_tree.py"""

    def test_find_leaves_of_binary_tree(self):
        s = Solution1()

        self.assertEqual([[4, 5, 3], [2], [1]], s.findLeaves(TreeNode.generate([1, 2, 3, 4, 5])))

    if __name__ == '__main__':
        unittest.main()

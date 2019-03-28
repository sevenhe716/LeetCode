import unittest

from BinaryTree.q222_count_complete_tree_nodes import Solution
from common import TreeNode


class TestCountCompleteTreeNodes(unittest.TestCase):
    """Test q222_count_complete_tree_nodes.py"""

    def test_count_complete_tree_nodes(self):
        s = Solution()

        self.assertEqual(0, s.countNodes(TreeNode.generate([])))
        self.assertEqual(6, s.countNodes(TreeNode.generate([1, 2, 3, 4, 5, 6])))


if __name__ == '__main__':
    unittest.main()

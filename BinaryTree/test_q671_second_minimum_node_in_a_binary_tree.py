import unittest

from BinaryTree.q671_second_minimum_node_in_a_binary_tree import Solution
from common import TreeNode


class TestSecondMinimumNodeInABinaryTree(unittest.TestCase):
    """Test q671_second_minimum_node_in_a_binary_tree.py"""

    def test_second_minimum_node_in_a_binary_tree(self):
        s = Solution()

        self.assertEqual(5, s.findSecondMinimumValue(TreeNode.generate([2, 2, 5, None, None, 5, 7])))
        self.assertEqual(-1, s.findSecondMinimumValue(TreeNode.generate([2, 2, 2])))
        self.assertEqual(8, s.findSecondMinimumValue(TreeNode.generate([5, 8, 5])))


if __name__ == '__main__':
    unittest.main()

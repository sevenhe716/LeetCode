import unittest

from Tree.q543_diameter_of_binary_tree import Solution
from common import TreeNode


class TestDiameterOfBinaryTree(unittest.TestCase):
    """Test q543_diameter_of_binary_tree.py"""

    def test_diameter_of_binary_tree(self):
        s = Solution()

        self.assertEqual(3, s.diameterOfBinaryTree(TreeNode.generate([1, 2, 3, 4, 5])))
        self.assertEqual(0, s.diameterOfBinaryTree(TreeNode.generate([])))
        self.assertEqual(0, s.diameterOfBinaryTree(TreeNode.generate([1])))
        self.assertEqual(1, s.diameterOfBinaryTree(TreeNode.generate([1, 2])))


if __name__ == '__main__':
    unittest.main()

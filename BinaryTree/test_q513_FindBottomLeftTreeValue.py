import unittest

from BinaryTree.q513_find_bottom_left_tree_value import Solution
from common import TreeNode


class TestFindBottomLeftTreeValue(unittest.TestCase):
    """Test q513_find_bottom_left_tree_value.py"""

    def test_find_bottom_left_tree_value(self):
        s = Solution()

        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(1, s.findBottomLeftValue(root))

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.left.left = TreeNode(7)
        root.right.right = TreeNode(6)
        self.assertEqual(7, s.findBottomLeftValue(root))


if __name__ == '__main__':
    unittest.main()

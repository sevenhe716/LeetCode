import unittest

from BinaryTree.q226_invert_binary_tree import Solution
from common import TreeNode


class TestInvertBinaryTree(unittest.TestCase):
    """Test q226_invert_binary_tree.py"""

    def test_invert_binary_tree(self):
        s = Solution()

        self.assertEqual(TreeNode.generate([4, 7, 2, 9, 6, 3, 1]), s.invertTree(TreeNode.generate([4, 2, 7, 1, 3, 6, 9])))


if __name__ == '__main__':
    unittest.main()

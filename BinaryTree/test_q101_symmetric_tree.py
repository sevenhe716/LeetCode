import unittest

from BinaryTree.q101_symmetric_tree import Solution
from common import TreeNode


class TestSymmetricTree(unittest.TestCase):
    """Test q101_symmetric_tree.py"""

    def test_symmetric_tree(self):
        s = Solution()

        self.assertEqual(True, s.isSymmetric(TreeNode.generate([1, 2, 2, 3, 4, 4, 3])))
        self.assertEqual(False, s.isSymmetric(TreeNode.generate([1, 2, 2, None, 3, None, 3])))


if __name__ == '__main__':
    unittest.main()

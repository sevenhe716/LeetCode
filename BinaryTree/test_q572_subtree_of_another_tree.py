import unittest

from BinaryTree.q572_subtree_of_another_tree import Solution
from common import TreeNode


class TestSubtreeOfAnotherTree(unittest.TestCase):
    """Test q572_subtree_of_another_tree.py"""

    def test_subtree_of_another_tree(self):
        s = Solution()

        self.assertEqual(True, s.isSubtree(TreeNode.generate([3, 4, 5, 1, 2]), TreeNode.generate([4, 1, 2])))
        self.assertEqual(False, s.isSubtree(TreeNode.generate([3, 4, 5, 1, 2, None, None, None, None, 0]), TreeNode.generate([4, 1, 2])))


if __name__ == '__main__':
    unittest.main()

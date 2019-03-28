import unittest

from BinaryTree.q250_count_univalue_subtrees import Solution
from common import TreeNode


class TestCountUnivalueSubtrees(unittest.TestCase):
    """Test q250_count_univalue_subtrees.py"""

    def test_count_univalue_subtrees(self):
        s = Solution()

        self.assertEqual(4, s.countUnivalSubtrees(TreeNode.generate([5, 1, 5, 5, 5, None, 5])))


if __name__ == '__main__':
    unittest.main()

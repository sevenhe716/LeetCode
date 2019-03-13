import unittest

from Tree.q538_convert_bst_to_greater_tree import Solution
from common import TreeNode


class TestConvertBstToGreaterTree(unittest.TestCase):
    """Test q538_convert_bst_to_greater_tree.py"""

    def test_convert_bst_to_greater_tree(self):
        s = Solution()

        self.assertEqual(TreeNode.generate([18, 20, 13]), s.convertBST(TreeNode.generate([5, 2, 13])))


if __name__ == '__main__':
    unittest.main()

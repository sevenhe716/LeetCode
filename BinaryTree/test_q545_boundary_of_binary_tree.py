import unittest

from BinaryTree.q545_boundary_of_binary_tree import Solution
from common import TreeNode


class TestBoundaryOfBinaryTree(unittest.TestCase):
    """Test q545_boundary_of_binary_tree.py"""

    def test_boundary_of_binary_tree(self):
        s = Solution()

        self.assertEqual([1, 3, 4, 2], s.boundaryOfBinaryTree(TreeNode.generate([1, None, 2, None, None, 3, 4])))
        self.assertEqual([1, 2, 4, 7, 8, 9, 10, 6, 3], s.boundaryOfBinaryTree(TreeNode.generate([1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10])))
        self.assertEqual([1], s.boundaryOfBinaryTree(TreeNode.generate([1])))

if __name__ == '__main__':
    unittest.main()

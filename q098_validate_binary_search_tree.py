# Time:  O(n)
# Space: O(1)

# 解题思路：
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        if root.left and root.left.val >= root.val:
                return False
        if root.right and root.right.val <= root.val:
                return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

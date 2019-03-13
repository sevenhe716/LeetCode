# Time:  O(n)
# Space: O(1)

# 解题思路：
# 是否基于原树去修改


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common import TreeNode


class Solution:
    # 不修改原树
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        if not t1 and not t2:
            return None
        t = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        t.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        t.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return t


class Solution1:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)

        return root

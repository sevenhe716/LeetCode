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
    def isSubtree(self, s: 'TreeNode', t: 'TreeNode') -> bool:
        def is_equal(t1, t2):
            # 指向同一个节点或者都为空时
            if t1 == t2:
                return True
            # 一个为空一个不为空，或者二者值不相等时
            if not t1 or not t2 or t1.val != t2.val:
                return False
            return is_equal(t1.left, t2.left) and is_equal(t1.right, t2.right)
        if not s:
            return t is None
        else:
            return is_equal(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


class Solution1:
    # 思路差不多，整体递归
    def isSubtree(self, s: 'TreeNode', t: 'TreeNode') -> 'bool':
        def dfs(a, b):
            if not a or not b:
                return not a and not b

            if a.val == b.val and dfs(a.left, b.left) and dfs(a.right, b.right):
                return True

            if b is t:
                return dfs(a.left, t) or dfs(a.right, t)

            return dfs(a, t)

        return dfs(s, t)
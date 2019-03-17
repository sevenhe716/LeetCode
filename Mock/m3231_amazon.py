# Time:  O(n)
# Space: O(1)

# Ideas:
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> bool:

        def dfs(root):
            if not root:
                return True, float('inf'), float('-inf')
            left_valid, left_min, left_max = dfs(root.left)
            right_valid, right_min, right_max = dfs(root.right)

            if not left_valid or not right_valid:
                return False, None, None

            if root.val <= left_max or root.val >= right_min:
                return False, None, None

            return True, min(left_min, right_min, root.val), max(left_max, right_max, root.val)

        res, _, _ = dfs(root)
        return res

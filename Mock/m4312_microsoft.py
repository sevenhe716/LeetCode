# Time:  O(n)
# Space: O(n)

# Ideas:
# dfs


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def dfs(root):
            find_p, find_q = False, False

            if root == p:
                find_p = True
            if root == q:
                find_q = True

            if root.left:
                left_find_p, left_find_q = dfs(root.left)
                find_p = find_p or left_find_p
                find_q = find_q or left_find_q
            if root.right:
                right_find_p, right_find_q = dfs(root.right)
                find_p = find_p or right_find_p
                find_q = find_q or right_find_q
            if find_p and find_q and not self.res:
                self.res = root
            return find_p, find_q

        dfs(root)
        return self.res


# Time:  O(n)
# Space: O(1)

# 解题思路：
# 求深度，计算每个节点的左右子树height之和的最大值


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: 'TreeNode') -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            left_height, right_height = dfs(root.left), dfs(root.right)
            self.res = max(self.res, left_height + right_height)
            return max(left_height, right_height) + 1

        dfs(root)
        return self.res

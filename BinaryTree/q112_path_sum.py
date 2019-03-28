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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(node, cur_sum):
            if not node.left and not node.right:
                return sum == cur_sum + node.val

            return (dfs(node.left, cur_sum + node.val) if node.left else False) or \
                   (dfs(node.right, cur_sum + node.val) if node.right else False)

        if not root:
            return False
        return dfs(root, 0)


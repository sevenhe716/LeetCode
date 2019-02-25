# Time:  O(n)
# Space: O(1)

# 解题思路：
# 遍历并识别所有的左叶子节点即可，左叶子节点即上一层来自左节点


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: 'TreeNode') -> 'int':
        def dfs(root, is_left):
            if not root:
                return 0

            return root.val if not root.left and not root.right and is_left else 0 + \
                dfs(root.left, True) + dfs(root.right, False)

        return dfs(root, False)
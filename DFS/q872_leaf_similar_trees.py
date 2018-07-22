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
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def dfs(root, seq):
            if not root.left and not root.right:
                seq.append(root)

            if root.left:
                dfs(root.left)

            if root.right:
                dfs(root.right)

        seq1, seq2 = [], []

        dfs(root1, seq1)
        dfs(root2, seq2)

        return seq1 == seq2

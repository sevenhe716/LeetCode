# Time:  O(n)
# Space: O(1)

# Ideas:
# try to find the last point in last level, didn't find a solution better than dfs or bfs


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: 'TreeNode') -> int:
        self.count = 0
        def dfs(root):
            if not root:
                return
            self.count += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.count
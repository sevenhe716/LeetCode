# Time:  O(n)
# Space: O(1)

# Ideas:
# try to find the last point in last level, didn't find a solution better than dfs or bfs
# mark


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


# compare the depth between left sub tree and right sub tree.
# A, If it is equal, it means the left sub tree is a full binary tree
# B, It it is not , it means the right sub tree is a full binary tree
# O(log(n) * log(n))
class Solution1:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
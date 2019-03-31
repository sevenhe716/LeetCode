# Time:  O(n)
# Space: O(1)

# 解题思路：
# 递归，BFS，DFS（等效于自定义栈迭代版的递归）


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root

    # recursively
    def invertTree1(self, root):
        if root:
            root.left, root.right = self.invertTree1(root.right), self.invertTree1(root.left)
            return root
        # 很漂亮的写法，不返回的分支等效于return None

    # BFS
    def invertTree2(self, root: 'TreeNode') -> 'TreeNode':
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # 允许node为None加入队列，为了融合边界条件
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

    # DFS
    def invertTree3(self, root: 'TreeNode') -> 'TreeNode':
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
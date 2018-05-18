# Time:  O(n)
# Space: O(1)

# 解题思路：
# DFS中序，用一个list维护每一层的最左节点，只添加一次因为第一次是最左

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # DFS recursion
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_values = []
        self.findBottomLeftValueR(root, 1, left_values)

        return left_values[-1]

    def findBottomLeftValueR(self, root, depth, left_values):
        if len(left_values) == depth - 1:
            left_values.append(root.val)

        if root.left:
            self.findBottomLeftValueR(root.left, depth + 1, left_values)

        if root.right:
            self.findBottomLeftValueR(root.right, depth + 1, left_values)


class SolutionF:
    # BFS non-recursion
    def findBottomLeftValue(self, root):
        from collections import deque

        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque([])
        queue.append(root)

        def bfs():
            while len(queue):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            return node.val

        return self.bfs()

    # DFS non-recursion
    def findBottomLeftValue2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [(root, 1)]
        cur = (root, 1)
        while q:
            node, depth = q.pop(0)
            if depth > cur[1]:
                cur = (node, depth)
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        return cur[0].val

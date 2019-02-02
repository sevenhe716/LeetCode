# Time:  O(n)
# Space: O(1)

# 解题思路：
# BFS遍历，再倒序插入即可
# 优化思路，deque比list慢，无需使用deque，insert(0)也很慢，可以最后利用[::-1]统一倒序即可

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret, dq, cur_nodes = [], deque(), [root]
        while cur_nodes:
            ret.insert(0, [node.val for node in cur_nodes])
            dq.extend(cur_nodes)
            cur_nodes = []
            while dq:
                node = dq.popleft()
                if node.left:
                    cur_nodes.append(node.left)
                if node.right:
                    cur_nodes.append(node.right)

        return ret


class Solution1:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, cur = [], [root]
        while cur:
            nextLevel, temp = [], []
            for node in cur:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                temp.append(node.val)
            cur = nextLevel
            res.append(temp)
        return res[::-1]